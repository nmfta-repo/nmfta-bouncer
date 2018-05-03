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


import auth, whitelist

class AuthTest(Resource):
  @jwt_required
  def get(self):
    return {"test":"response"}

api.add_resource(auth.Login, "/login")
api.add_resource(auth.Register, "/register")
api.add_resource(AuthTest, "/authtest")



if __name__ == '__main__':
  if "--clear" in sys.argv:
    database.clear_data()
    exit()
  app.run(debug=True, port=8080)
