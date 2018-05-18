"""This module is the main app for the firewall"""

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import DB
import auth
import firewall

VERSION = 1

#Initialize Flask API and Create DB
APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
APP.config['SECRET_KEY'] = 'some-secret-string'	#should also probably change this
DB.init_app(APP)
DB.create_all(app=APP)
APP.config['JWT_SECRET_KEY'] = 'jwt-secret-string' #should probably change this
JWT = JWTManager(APP)
API = Api(APP, prefix="/v{}".format(VERSION))

#Add resources and endpoints to facilitate RESTful paradigm

#add auth module
API.add_resource(auth.Login, "/login")
API.add_resource(auth.Register, "/register") #testing only

#add firewall modules
#add whitelist module
API.add_resource(
    firewall.IpGeoList, "/whitelists",
    resource_class_kwargs={"ltype":"wl"}, endpoint="wlgl")
API.add_resource(
    firewall.IpList, "/whitelists/ipaddresses",
    resource_class_kwargs={"ltype":"wl"}, endpoint="wl")
API.add_resource(
    firewall.EntrySearch, "/whitelists/ipaddresses/filter/<string:filter>",
    resource_class_kwargs={"ltype":"wl"}, endpoint="wlf")
API.add_resource(
    firewall.Entry, "/whitelists/ipaddresses/<string:entry>",
    resource_class_kwargs={"ltype":"wl"}, endpoint="wle")
API.add_resource(
    firewall.CreateIpEntry, "/whitelists/create",
    resource_class_kwargs={"ltype":"wl"}, endpoint="wlc")

#add blacklist module
API.add_resource(
    firewall.IpGeoList, "/blacklists",
    resource_class_kwargs={"ltype":"bl"}, endpoint="blgl")
API.add_resource(
    firewall.IpList, "/blacklists/ipaddresses",
    resource_class_kwargs={"ltype":"bl"}, endpoint="bl")
API.add_resource(
    firewall.EntrySearch, "/blacklists/ipaddresses/filter/<string:filter>",
    resource_class_kwargs={"ltype":"bl"}, endpoint="blf")
API.add_resource(
    firewall.Entry, "/blacklists/ipaddresses/<string:entry>",
    resource_class_kwargs={"ltype":"bl"}, endpoint="ble")
API.add_resource(
    firewall.CreateIpEntry, "/blacklists/create",
    resource_class_kwargs={"ltype":"bl"}, endpoint="blc")


if __name__ == '__main__':
    APP.run(debug=True, port=8080)
