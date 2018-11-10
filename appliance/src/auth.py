"""Auth module for the firewall app"""

from datetime import timedelta
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token)
from models import UserModel

PARSER = reqparse.RequestParser()
PARSER.add_argument("username")
PARSER.add_argument("password")
PARSER.add_argument("grant_type")

class Register(Resource):
    """Register Class"""
    @classmethod
    def post(cls):
        """Handles post register requests"""
        data = PARSER.parse_args()
        if UserModel.lookup_user(data['username']):
            return jsonify(message='user already exists')
        user = UserModel(
            username=data['username'],
            password=UserModel.gen_hash(data['password']))
        user.save()
        return jsonify(message='all good with user creation')

class Login(Resource):
    """Login Class"""
    @classmethod
    def post(cls):
        """Handles post login requests"""
        exp_time = timedelta(days=0, hours=0, minutes=10) #set token valid time to 10 minutes
        data = PARSER.parse_args()
        user = UserModel.lookup_user(data['username'])
        if data['grant_type'] != 'password':
            return jsonify(message='incorrect grant_type')

        if not user:
            return jsonify(message='User does not exist')

        if UserModel.verify_hash(data['password'], user.password):
            access_token = create_access_token(identity=data['username'], expires_delta=exp_time)
            return jsonify(
                access_token=access_token,
                token_type="bearer",
                expires_in=600,
                claim_level="complete"
            )
        return jsonify(message='failed to log in')

class BrokenHTTPS(Resource):
    """BrokenHTTPS Class"""
    @classmethod
    def post(cls):
        """Handles post login requests if a valid HTTPS cert isn't found"""
        return jsonify(message='Valid HTTPS cert does not exist')
