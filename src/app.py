from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import sys, database

version = 1

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)
api = Api(app, prefix="/v{}".format(version))
database.init_db(app)

import auth, firewall

#add auth module
api.add_resource(auth.Login, "/login")
api.add_resource(auth.Register, "/register") #testing only

#add firewall modules
#add whitelist module
api.add_resource(firewall.IpGeoList, "/whitelists", resource_class_kwargs={"ltype":"wl"}, endpoint="wlgl")
api.add_resource(firewall.IpList, "/whitelists/ipaddresses", resource_class_kwargs={"ltype":"wl"}, endpoint="wl")
api.add_resource(firewall.EntrySearch, "/whitelists/ipaddresses/<string:filter>", resource_class_kwargs={"ltype":"wl"}, endpoint="wlf")
api.add_resource(firewall.CreateIpEntry, "/whitelists/create", resource_class_kwargs={"ltype":"wc"})

#add blacklist module
api.add_resource(firewall.IpGeoList, "/blacklists", resource_class_kwargs={"ltype":"bl"}, endpoint="blgl")
api.add_resource(firewall.IpList, "/blacklists/create", resource_class_kwargs={"ltype":"bl"}, endpoint="bl")
api.add_resource(firewall.CreateIpEntry, "/blacklists/create", resource_class_kwargs={"ltype":"bl"}, endpoint="bc")


if __name__ == '__main__':
        if "--clear" in sys.argv:
                database.clear_data()
                exit()
        app.run(debug=True, port=8080)
