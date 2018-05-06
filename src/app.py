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

import auth, whitelist, blacklist

#add auth module
api.add_resource(auth.Login, "/login")
api.add_resource(auth.Register, "/register") #testing only

#add firewall modules
#add whitelist module
api.add_resource(whitelist.Whitelists, "/whitelists")
api.add_resource(whitelist.WhitelistsCreate, "/whitelists/create")
#add blacklist module
api.add_resource(blacklist.Blacklists, "/blacklists")
api.add_resource(blacklist.BlacklistsCreate, "/blacklists/create")


if __name__ == '__main__':
		if "--clear" in sys.argv:
				database.clear_data()
				exit()
		app.run(debug=True, port=8080)
