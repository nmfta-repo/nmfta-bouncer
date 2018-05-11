import sys
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import database

VERSION = 1

#Initialize Flask API and Create DB
APP = Flask(__name__)
APP.config['JWT_SECRET_KEY'] = 'jwt-secret-string' #should probably change this
JWT = JWTManager(APP)
API = Api(APP, prefix="/v{}".format(VERSION))
database.init_db(APP)

'''
Import Auth and Firewall modules`
#If we try to import them sooner, they do
not have the DB built and crash
'''

import auth
import firewall

#Add resources and endpoints to facilitate RESTful paradigm

#add auth module
API.add_resource(auth.Login, "/login")
API.add_resource(auth.Register, "/register") #testing only

#add firewall modules
#add whitelist module
API.add_resource(firewall.IpGeoList, "/whitelists", resource_class_kwargs={"ltype":"wl"}, endpoint="wlgl")
API.add_resource(firewall.IpList, "/whitelists/ipaddresses", resource_class_kwargs={"ltype":"wl"}, endpoint="wl")
API.add_resource(firewall.EntrySearch, "/whitelists/ipaddresses/filter/<string:filter>", resource_class_kwargs={"ltype":"wl"}, endpoint="wlf")
API.add_resource(firewall.Entry, "/whitelists/ipaddresses/<string:entry>", resource_class_kwargs={"ltype":"wl"}, endpoint="wle")
API.add_resource(firewall.CreateIpEntry, "/whitelists/create", resource_class_kwargs={"ltype":"wl"}, endpoint="wlc")

#add blacklist module
API.add_resource(firewall.IpGeoList, "/blacklists", resource_class_kwargs={"ltype":"bl"}, endpoint="blgl")
API.add_resource(firewall.IpList, "/blacklists/ipaddresses", resource_class_kwargs={"ltype":"bl"}, endpoint="bl")
API.add_resource(firewall.EntrySearch, "/blacklists/ipaddresses/filter/<string:filter>", resource_class_kwargs={"ltype":"bl"}, endpoint="blf")
API.add_resource(firewall.Entry, "/blacklists/ipaddresses/<string:entry>", resource_class_kwargs={"ltype":"bl"}, endpoint="ble")
API.add_resource(firewall.CreateIpEntry, "/blacklists/create", resource_class_kwargs={"ltype":"bl"}, endpoint="blc")


if __name__ == '__main__':
    #dev feature to clear the database
    if "--clear" in sys.argv:
        database.clear_data()
        exit()
    APP.run(debug=True, port=8080)
