from flask import Flask,jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import BLModel, WLModel
#import netaddr

parser = reqparse.RequestParser()
parser.add_argument("IPv4", required=False)
parser.add_argument("IPv6", required=False)
parser.add_argument("Start_Date", required=False)
parser.add_argument("End_Date", required=False)
parser.add_argument("Comments", required=False)
parser.add_argument("Active", required=False)

class Checker():
    def __init__(self, ltype):
        self.ltype = ltype
    #check if request is WList or BList
    def type_test(self):
        return WLModel if self.ltype is "wl" else BLModel

class IpGeoList(Checker, Resource):
    #Match List IP/Geo Entries
    @jwt_required
    def get(self):
        mod = self.type_test()
        return jsonify(
            Result = {
                "Status":"Success",
                "Message":"Showing All IPs and Geo"
            },
            IPAddresses=mod.get_all_ip(),
            GeoLocations=[]
        )

class IpList(Checker, Resource):
    #Match List IP Entries
    @jwt_required
    def get(self):
        mod = self.type_test()
        return jsonify(
            Result = {
                "Status":"Success",
                "Message":"Showing All IPs"
            },
            IPAddresses=mod.get_all_ip(),
        )

class EntrySearch(Checker, Resource):
    #Search for Matching Entry
    @jwt_required
    def get(self, filter):
        mod = self.type_test()
        search_results = []
        for ip in str(filter).split(","):
            if "/" in ip:
                #do cidr calc
                pass
            t = mod.search(ip)
            if t:
                search_results.append(t.ipv4)
        return jsonify(
            Result = {
                "Status":"Success",
                "Message":"Showing All Matching"
            },
            SearchResult = {
                "Input_IP":filter,
                "Entries":search_results
            }
        )

class Entry(Checker, Resource):
    #Search for Matching Entry
    @jwt_required
    def get(self, entry):
        mod = self.type_test()
        info = mod.search(entry)
        if info is not None:
            return jsonify(
                Result = {
                    "Status":"Success",
                    "Message":"Showing Matching Entry"
                },
                Entry={
                "IPv4":info.ipv4, "IPv6":info.ipv6, "Start_Date":info.start_date,
                    "End_Date":info.end_date, "Comments":info.comments, "Active":info.active}
            )
        return jsonify(
            Result = {
                "Status":"Error",
                "Message":"No Matching Entry"
            }
        )

class CreateIpEntry(Checker, Resource):
    @jwt_required
    def post(self):
        mod = self.type_test()
        data = parser.parse_args()
        ip = ""
        ip = data["IPv4"] if data["IPv4"] else ""
        ip = data["IPv6"] if data["IPv6"] else ip
        if ip is "":
            return jsonify(
                Result = {
                    "Status":"Invalid",
                    "Message":"Must enter IPv4 or IPv6 address"
                 }
            )
        #check if already in database
        if BLModel.exists(ip) or WLModel.exists(ip):
            return jsonify(
                Result = {
                    "Status":"Error",
                    "Message":"IP exists in system"
                 }
            )
        new_ip = mod(ipv4 = data['IPv4'], ipv6 = data['IPv6'], start_date = data['Start_Date'],
            end_date = data['End_Date'], comments = data['Comments'], active = data["Active"])
        new_ip.save_to_db()
        return jsonify(
                Result = {
                        "Status":"Success",
                        "Message":"IP Added"
             }
        )
