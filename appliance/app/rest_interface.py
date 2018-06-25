"""This module is the manager app for the platform"""

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import DB
import argparse
import configparser
import auth
import manage

VERSION = 2


#Parse args and read config from configfile
parser = argparse.ArgumentParser(description="REST API for bouncer")
config = configparser.ConfigParser()
parser.add_argument("--testing", help="Enable testing features")
parser.add_argument("--config", help="Specify config file to read from",
    default="/home/marcus/.bouncer/default.conf")
args = parser.parse_args()
config.read(args.config)


#Initialize Flask API and Create DB
APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+config['DEFAULT']['dbname']
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
APP.config['SECRET_KEY'] = config['DEFAULT']['secretkey']
DB.init_app(APP)
DB.create_all(app=APP)
APP.config['JWT_SECRET_KEY'] = config['DEFAULT']['jwtsecretkey']
JWT = JWTManager(APP)
API = Api(APP, prefix="/v{}".format(VERSION))

#Add resources and endpoints to facilitate RESTful paradigm

#add auth module
API.add_resource(auth.Login, "/login")

#enable testing features
if args.testing:
    API.add_resource(auth.Register, "/register")

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
    manage.CreateIpEntry, "/whitelists/create",
    resource_class_kwargs={"ltype":"wl"}, endpoint="wlc")

#add blacklist module
API.add_resource(
    manage.Lists, "/blacklists",
    resource_class_kwargs={"ltype":"bl"}, endpoint="blgl")
API.add_resource(
    manage.IpList, "/blacklists/ipaddresses",
    resource_class_kwargs={"ltype":"bl"}, endpoint="bl")
API.add_resource(
    manage.SearchIpList, "/blacklists/ipaddresses/filter/<string:filter>",
    resource_class_kwargs={"ltype":"bl"}, endpoint="blf")
API.add_resource(
    manage.IpEntry, "/blacklists/ipaddresses/<string:entry>",
    resource_class_kwargs={"ltype":"bl"}, endpoint="ble")
API.add_resource(
    manage.CreateIpEntry, "/blacklists/create",
    resource_class_kwargs={"ltype":"bl"}, endpoint="blc")


if __name__ == '__main__':
    APP.run(debug=True, port=config['DEFAULT']['port'], host=config['DEFAULT']['listenip'])
