"""This module is the manager app for the platform"""

from flask import Flask, jsonify, make_response
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import DB
import argparse
import configparser
import os
import auth
import manage
import random
import string
import secrets

VERSION = 1


#Parse args and read config from configfile
parser = argparse.ArgumentParser(description="REST API for bouncer")
config = configparser.ConfigParser()
parser.add_argument("--testing", help="Enable testing features", action="store_true")
parser.add_argument("--config", help="Specify config file to read from",
    default="/opt/bouncer/default.conf")
args = parser.parse_args()
config.read(args.config)


#Initialize Flask API and Create DB
APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+config['DEFAULT']['dbname']
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
APP.config['SECRET_KEY'] = secrets.token_urlsafe(32)
APP.config['PROPAGATE_EXCEPTIONS'] = True
DB.init_app(APP)
DB.create_all(app=APP)
APP.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(32)
JWT = JWTManager(APP)
API = Api(APP, prefix="/v{}".format(VERSION))

@JWT.expired_token_loader
def expired_callback():
    return make_response(jsonify({
        "Status":"TokenExpired",
        "Error":"9999"
    }), 400)

#Add resources and endpoints to facilitate RESTful paradigm

#if cert exists
if os.path.isfile(config['DEFAULT']['keypath']) and os.path.isfile(config['DEFAULT']['certpath']):
    #add auth module
    API.add_resource(auth.Login, "/login")

    #enable testing features
    if args.testing:
        API.add_resource(auth.Register, "/register")

    API.add_resource(manage.SimpleCheck, "/check/<string:entry>",
        resource_class_kwargs={"ltype":"wl"})

    #add firewall modules
    #add whitelist module
    API.add_resource(
        manage.Lists, "/whitelists",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wlgl")
    API.add_resource(
        manage.IpList, "/whitelists/ipaddresses",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wl")
    API.add_resource(
        manage.SearchIpList, "/whitelists/ipaddresses/filter/<string:filter_term>",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wlf")
    API.add_resource(
        manage.IpEntry, "/whitelists/ipaddresses/<string:entry>",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wle")
    API.add_resource(
        manage.UpdateIpEntry, "/whitelists/ipaddresses/<string:entry>/update",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wleu")
    API.add_resource(
        manage.CreateIpEntry, "/whitelists/ipaddresses/create",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wlc")
    API.add_resource(
        manage.DeleteIpEntry, "/whitelists/ipaddresses/<string:entry>/delete",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wld")
    API.add_resource(
        manage.GeoList, "/whitelists/geolocations",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wlg")
    API.add_resource(
        manage.CreateGeoEntry, "/whitelists/geolocations/create",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wlgc")
    API.add_resource(
        manage.GeoEntry, "/whitelists/geolocations/<string:entry>",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wlge")
    API.add_resource(
        manage.UpdateGeoEntry, "/whitelists/geolocations/<string:entry>/update",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wlgu")
    API.add_resource(
        manage.DeleteGeoEntry, "/whitelists/geolocations/<string:entry>/delete",
        resource_class_kwargs={"ltype":"wl"}, endpoint="wlgd")

    #add blacklist module
    API.add_resource(
        manage.Lists, "/blacklists",
        resource_class_kwargs={"ltype":"bl"}, endpoint="blgl")
    API.add_resource(
        manage.IpList, "/blacklists/ipaddresses",
        resource_class_kwargs={"ltype":"bl"}, endpoint="bl")
    API.add_resource(
        manage.SearchIpList, "/blacklists/ipaddresses/filter/<string:filter_term>",
        resource_class_kwargs={"ltype":"bl"}, endpoint="blf")
    API.add_resource(
        manage.IpEntry, "/blacklists/ipaddresses/<string:entry>",
        resource_class_kwargs={"ltype":"bl"}, endpoint="ble")
    API.add_resource(
        manage.CreateIpEntry, "/blacklists/ipaddresses/create",
        resource_class_kwargs={"ltype":"bl"}, endpoint="blc")
    API.add_resource(
        manage.DeleteIpEntry, "/blacklists/ipaddresses/<string:entry>/delete",
        resource_class_kwargs={"ltype":"bl"}, endpoint="bld")
    API.add_resource(
        manage.GeoList, "/blacklists/geolocations",
        resource_class_kwargs={"ltype":"bl"}, endpoint="blg")
    API.add_resource(
        manage.CreateGeoEntry, "/blacklists/geolocations/create",
        resource_class_kwargs={"ltype":"bl"}, endpoint="blgc")
    API.add_resource(
        manage.GeoEntry, "/blacklists/geolocations/<string:entry>",
        resource_class_kwargs={"ltype":"bl"}, endpoint="blge")
    API.add_resource(
        manage.UpdateGeoEntry, "/blacklists/geolocations/<string:entry>/update",
        resource_class_kwargs={"ltype":"bl"}, endpoint="blgu")
    API.add_resource(
        manage.DeleteGeoEntry, "/blacklists/geolocations/<string:entry>/delete",
        resource_class_kwargs={"ltype":"bl"}, endpoint="blgd")

    APP.run(ssl_context=(config['DEFAULT']['certpath'], config['DEFAULT']['keypath']), port=config['DEFAULT']['port'], host=config['DEFAULT']['listenip'])

else:
    print("Certs are not set correctly; disabling for security reasons")
    API.add_resource(auth.BrokenHTTPS, "/login")
    APP.run(port=config['DEFAULT']['port'], host=config['DEFAULT']['listenip'])
