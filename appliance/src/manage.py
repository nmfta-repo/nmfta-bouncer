"""Firewall module for the firewall app"""

from flask import jsonify, make_response
import netaddr
import math
import ipaddress
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models import IPModel, GeoModel

PARSER = reqparse.RequestParser()
PARSER.add_argument("CountryCode", required=False)
PARSER.add_argument("IPv4", required=False)
PARSER.add_argument("IPv6", required=False)
PARSER.add_argument("Start_Date", required=False)
PARSER.add_argument("End_Date", required=False)
PARSER.add_argument("Comments", required=False)
PARSER.add_argument("Active", required=False)

class Checker(object): # pylint: disable=too-few-public-methods
    """
    Check class allows switching between Whitelist and Blacklist
    from the Resource call by switching a Class variable from "wl" to "bl"
    This lets us use the same CRUD functions for Whitelist and Blacklist
    Maximizes code reuse while maintaining flexibility
    """
    def __init__(self, ltype):
        self.ltype = ltype

class SimpleCheck(Checker, Resource):
    @jwt_required
    def get(self, entry):
        """Handles get Entry requests"""
        try:
            ipaddress.ip_address(entry)
        except:
            if self.ltype is "wl":
                return make_response(jsonify(Result={"Status":"Error","Message":"IP Invalid"}), 400)

        wl = IPModel.search(entry, "wl")
        bl = IPModel.search(entry, "bl")
        if bl is None and wl is None:
            return make_response(jsonify(Result={"Status":"Success","Message":"No Matching Entry"}), 400)

        info = wl if wl else bl
        ltype = "Whitelist" if wl else "Blacklist"
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Showing Matching Entry",
                "List":ltype
            },
            Entry={
                "IPv4":info.ipv4, "IPv6":info.ipv6, "Start_Date":info.start_date,
                "End_Date":info.end_date, "Comments":info.comments, "Active":info.active}
        )


class Lists(Checker, Resource):
    """This provides an array of whitelist (1...n) entries. The Whitelists
    should include both the IP Address Entries and Geolocation Entries"""
    @jwt_required
    def get(self):
        """Handles get IpGeoList requests"""
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Showing All IPs and Geo"
            },
            IPAddresses=IPModel.get_all_ip(self.ltype),
            GeoLocations=GeoModel.get_all_geo(self.ltype)
        )

class IpList(Checker, Resource):
    """This provides an array of whitelisted IP Addresses."""
    @jwt_required
    def get(self):
        """Handles get IpList requests"""
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Showing All IPs"
            },
            IPAddresses=IPModel.get_all_ip(self.ltype),
        )

class SearchIpList(Checker, Resource):
    """This provides an end-point to look for the whitelisted IP Addresses.
    """
    @jwt_required
    def get(self, filter_term):
        """Handles get EntrySearch requests
        CIDR addresses need to be passed with + instead of /
        as / breaks the REST implimentation"""
        search_results = []
        for search_ip in str(filter_term).split(","):
            if "+" in search_ip:
                search_ip = search_ip.replace("+", "/")
                for sub_ip in netaddr.IPNetwork(search_ip).iter_hosts():
                    found_ip = IPModel.search(str(sub_ip), self.ltype)
                    if found_ip:
                        search_results.append((str(found_ip.id),found_ip.ipv4))
            else:
                found_ip = IPModel.search(search_ip, self.ltype)
                if found_ip:
                    search_results.append((str(found_ip.id),found_ip.ipv4))
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Showing All Matching"
            },
            SearchResult={
                "Input_IP":search_ip,
                "Entries":search_results})

class IpEntry(Checker, Resource):
    """This provides detail information about an individual entry"""
    @jwt_required
    def get(self, entry):
        """Handles get Entry requests"""
        info = IPModel.get_entry(entry, self.ltype)
        if info is not None:
            return jsonify(
                Result={
                    "Status":"Success",
                    "Message":"Showing Matching Entry"
                },
                Entry={
                    "IPv4":info.ipv4, "IPv6":info.ipv6, "Start_Date":info.start_date,
                    "End_Date":info.end_date, "Comments":info.comments, "Active":info.active}
            )
        return make_response(jsonify(
            Result={
                "Status":"Error",
                "Message":"No Matching Entry"}), 400)

class CreateIpEntry(Checker, Resource):
    """This method is used to add a whitelist entry"""
    @jwt_required
    def post(self):
        """Handles post CreateIpEntry"""
        data = PARSER.parse_args()
        active = True
        entry_ip = data["IPv4"] if data["IPv4"] else ""
        entry_ip = data["IPv6"] if data["IPv6"] else entry_ip
        try:
            ipaddress.ip_address(entry_ip)
        except:
            if self.ltype is "wl":
                if not entry_ip:
                    return make_response(jsonify(Result={"Status":"Invalid","Error":"3000"}), 400)
                return make_response(jsonify(Result={"Status":"Invalid","Error":"3001"}), 400)
            else:
                if not entry_ip:
                    return make_response(jsonify(Result={"Status":"Invalid","Error":"4000"}), 400)
                return make_response(jsonify(Result={"Status":"Invalid","Error":"4001"}), 400)

        #check if IP exists in the system
        if IPModel.exists(entry_ip, "wl"):
            if self.ltype is "wl":
                return make_response(jsonify(Result={"Status":"Failed","Error":"3008"}), 400)
            else:
                return make_response(jsonify(Result={"Status":"Failed","Error":"3009"}), 400)
        if IPModel.exists(entry_ip, "bl"):
            if self.ltype is "bl":
                return make_response(jsonify(Result={"Status":"Failed","Error":"4008"}), 400)
            else:
                return make_response(jsonify(Result={"Status":"Failed","Error":"4009"}), 400)

        if data["Active"]:
            if data["Active"].lower() is "false" or data["Active"] is "0":
                active = False
            elif data["Active"].lower() is "true" or data["Active"] is "1":
                active = True

        if len(data['Comments']) > 3000:
            if self.ltype is "wl":
                return make_response(jsonify(Result={"Status":"Invalid","Error":"3007"}), 400)
            else:
                return make_response(jsonify(Result={"Status":"Invalid","Error":"4007"}), 400)

        new_ip = IPModel(lt=self.ltype, ipv4=data['IPv4'], ipv6=data['IPv6'], start_date=data['Start_Date'],
                     end_date=data['End_Date'], comments=data['Comments'], active=active, remove=False, geo=False)
        new_ip.save()
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"IP Added",
                "EntryID":str(new_ip.id)})

class UpdateIpEntry(Checker, Resource):
    """This method is used to update an existing list entry"""
    @jwt_required
    def put(self, entry):
        """Handles post UpdateIpEntry"""
        data = PARSER.parse_args()
        entry_id = IPModel.update_entry(entry, data, self.ltype)
        if not entry:
            return make_response(jsonify(
                Result={
                    "Status":"Error",
                    "Message":"No Matching Entry"}), 400)
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"IP Updated",
                "EntryID":str(entry_id)})


class DeleteIpEntry(Checker, Resource):
    """This method is used to delete a listed entry"""
    @jwt_required
    def delete(self, entry):
        """Handles delete DeleteIpEntry"""
        if not entry:
            if self.ltype is "wl":
                return make_response(jsonify(Result={"Status":"Invalid","Error":"5000"}), 400)
            else:
                return make_response(jsonify(Result={"Status":"Invalid","Error":"6000"}), 400)
        entry_id = IPModel.delete_entry(entry, self.ltype)
        if not entry_id:
            if self.ltype is "wl":
                return make_response(jsonify(Result={"Status":"Invalid","Error":"5001"}), 400)
            else:
                return make_response(jsonify(Result={"Status":"Invalid","Error":"6001"}), 400)
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"IP Deleted",
                "EntryID":str(entry_id)})

class GeoList(Checker, Resource):
    """This provides an array of listed Geolocation Entries"""
    @jwt_required
    def get(self):
        """Handles get GeoList requests"""
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Showing All Geo"
            },
            GeoLocations=GeoModel.get_all_geo(self.ltype),
        )

class CreateGeoEntry(Checker, Resource):
    """This creates GeoIP entries"""
    @jwt_required
    def post(self):
        """Handles creation of GeoCreate requests"""
        data = PARSER.parse_args()
        active = True
        if not data['CountryCode']:
            return make_response(jsonify(
                Result={
                    "Status":"Error",
                    "Message":"Valid ISO required"}), 400)

        if GeoModel.exists(data['CountryCode']):
            return make_response(jsonify(
                Result={
                    "Status":"Error",
                    "Message":"ISO Exists in DB"}), 400)

        if data["Active"]:
            if data["Active"].lower() is "false" or data["Active"] is "0":
                active = False
            elif data["Active"].lower() is "true" or data["Active"] is "1":
                active = True

        new_geo = GeoModel(lt=self.ltype, cc=data['CountryCode'], start_date=data['Start_Date'],
                    end_date=data['End_Date'], comments=data['Comments'], active=active, remove=False)
        new_geo.save()

        f = open("geolist.txt")
        lines = f.readlines()
        for line in lines:
            if (('ipv4' in line) & (new_geo.cc in line)) :
                s=line.split("|")
                net=s[3]
                cidr=float(s[4])
                ip4 = "%s/%d" % (net,(32-math.log(cidr,2)))
                new_ip = IPModel(lt=self.ltype, ipv4=ip4, geo=new_geo.id, remove=False)
                new_ip.save()

        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Geo Added",
                "EntryID":str(new_geo.id)
            })

class GeoEntry(Checker, Resource):
    """This provides detail information about an individual whitelisted geo entry"""
    @jwt_required
    def get(self, entry):
        """Handles get geo Entry requests"""
        info = GeoModel.get_entry(entry, self.ltype)
        if info is not None:
            return jsonify(
                Result={
                    "Status":"Success",
                    "Message":"Showing Matching Entry"
                },
                Entry={
                    "Country Code":info.cc, "Start_Date":info.start_date,
                    "End_Date":info.end_date, "Comments":info.comments, "Active":info.active}
            )
        return make_response(jsonify(
            Result={
                "Status":"Error",
                "Message":"No Matching Entry"}), 400)

class UpdateGeoEntry(Checker, Resource):
    """This method is used to update an existing list entry"""
    @jwt_required
    def post(self, entry):
        """Handles post UpdateGeoEntry"""
        data = PARSER.parse_args()
        entry_id = GeoModel.update_entry(entry, data, self.ltype)
        if not entry:
            return make_response(jsonify(
                Result={
                    "Status":"Error",
                    "Message":"No Matching Entry"}), 400)
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Geo Updated",
                "EntryID":str(entry_id)})

class DeleteGeoEntry(Checker, Resource):
    """This method is used to delete a listed entry"""
    @jwt_required
    def DELETE(self, entry):
        """Handles delete DeleteGeoEntry"""
        data = PARSER.parse_args()
        entry_id = GeoModel.delete_entry(entry, self.ltype)
        if not entry:
            return make_response(jsonify(
                Result={
                    "Status":"Error",
                    "Message":"No Matching Entry"}), 400)
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Geo Deleted",
                "EntryID":str(entry_id)})
