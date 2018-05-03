from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from models import IPModel

parser = reqparse.RequestParser()
parser.add_argument("IPv4", required=False)
parser.add_argument("IPv6", required=False)
parser.add_argument("Start_Date", required=False)
parser.add_argument("End_Date", required=False)
parser.add_argument("Comments", required=False)
parser.add_argument("Active", required=False)

class Whitelists(Resource):
  @jwt_required
  def get(self):
    return {
      "Result":{
        "Status":"Success",
        "Message":"Showing All Whitelisted IPs"
      },
      "IPAddresses":IPModel.get_all_ip()
    }
class WhitelistsCreate(Resource):
  @jwt_required
  def post(self):
    data = parser.parse_args()
    ip = ""
    ip = data["IPv4"] if data["IPv4"] else ""
    ip = data["IPv6"] if data["IPv6"] else ip
    if ip is "":
      return {
        "Result":{
          "Status":"Invalid",
           "Message":"Must enter IPv4 or IPv6 address"
         }
      }
      
    #check if already in database
    if IPModel.exists_in_database(ip):
      return {
        "Result":{
          "Status":"Error",
           "Message":"IP exists in system"
         }
      }
      
    #insert new IP into database as whitelisted value
    new_ip = IPModel(ipv4 = data['IPv4'], ipv6 = data['IPv6'], start_date = data['Start_Date'],
      end_date = data['End_Date'], comments = data['Comments'], active = data["Active"], access_list = "whitelist")
    new_ip.save_to_db()
    #actually add to firewall code (system command maybe?)
    return {
      "Result":{
        "Status":"Success",
        "Message":"IP Added to whitelist"
       }
    }
      
    
    
    
