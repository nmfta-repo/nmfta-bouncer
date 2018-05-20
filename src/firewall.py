"""Firewall module for the firewall app"""

from flask import jsonify
import netaddr
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models import BLModel, WLModel

PARSER = reqparse.RequestParser()
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
    """check if request is WList or BList"""
    def type_test(self):
        """Check if requester is looking for white/black list"""
        return WLModel if self.ltype == "wl" else BLModel

class IpGeoList(Checker, Resource):
    """IpGeoList Class"""
    @jwt_required
    def get(self):
        """Handles get IpGeoList requests"""
        mod = self.type_test()
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Showing All IPs and Geo"
            },
            IPAddresses=mod.get_all_ip(),
            GeoLocations=[]
        )

class IpList(Checker, Resource):
    """IpList Class"""
    @jwt_required
    def get(self):
        """Handles get IpList requests"""
        mod = self.type_test()
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Showing All IPs"
            },
            IPAddresses=mod.get_all_ip(),
        )

class EntrySearch(Checker, Resource):
    """EntrySearch Class"""
    @jwt_required
    def get(self, filter_term):
        """Handles get EntrySearch requests
        CIDR addresses need to be passed with # instead of /
        as / breaks the REST implimentation"""
        mod = self.type_test()
        search_results = []
        for search_ip in str(filter_term).split(","):
            if "+" in search_ip:
                search_ip = search_ip.replace("+", "/")
                for sub_ip in netaddr.IPNetwork(search_ip).iter_hosts():
                    found_ip = mod.search(str(sub_ip))
                    if found_ip:
                        search_results.append(found_ip.ipv4)
            else:
                found_ip = mod.search(search_ip)
                if found_ip:
                    search_results.append(found_ip.ipv4)
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"Showing All Matching"
            },
            SearchResult={
                "Input_IP":filter_term,
                "Entries":search_results})

class Entry(Checker, Resource):
    """Entry Class"""
    @jwt_required
    def get(self, entry):
        """Handles get Entry requests"""
        mod = self.type_test()
        info = mod.search(entry)
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
        return jsonify(
            Result={
                "Status":"Error",
                "Message":"No Matching Entry"})

class CreateIpEntry(Checker, Resource):
    """CreateIpEntry Class"""
    @jwt_required
    def post(self):
        """Handles post CreateIpEntry"""
        mod = self.type_test()
        data = PARSER.parse_args()
        entry_ip = data["IPv4"] if data["IPv4"] else ""
        entry_ip = data["IPv6"] if data["IPv6"] else entry_ip
        if entry_ip == "":
            return jsonify(
                Result={
                    "Status":"Invalid",
                    "Message":"Must enter IPv4 or IPv6 address"})
        #check if already in database
        if BLModel.exists(entry_ip) or WLModel.exists(entry_ip):
            return jsonify(
                Result={
                    "Status":"Error",
                    "Message":"IP exists in system"})
        new_ip = mod(ipv4=data['IPv4'], ipv6=data['IPv6'], start_date=data['Start_Date'],
                     end_date=data['End_Date'], comments=data['Comments'], active=data["Active"])
        new_ip.save()
        return jsonify(
            Result={
                "Status":"Success",
                "Message":"IP Added"})
