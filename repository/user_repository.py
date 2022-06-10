from flask import request
from firebase_admin import auth
from firebase import app
from models.error import Error
from models.response import Response
from validators.email_validator import has_valid_email
from validators.password_validator import has_valid_password


class UserRepository:
    @has_valid_email
    @has_valid_password
    def create_user(self):
        data = request.json
        try:
            display_name = data['display_name']
        except NameError:
            display_name = None
        email = data['email']
        password = data['password']

        try:
            auth.create_user(
                display_name=display_name,
                email=email,
                password=password
            )
            return Response(200, 'User successfully signed up').serialize(), 200
        except NameError:
            return Error(500, 'User can not be signed up').serialize(), 500

    @has_valid_email
    def verify_email(self):
        data = request.json
        email = data['email']
        try:
            generated_link = auth.generate_email_verification_link(
                email=email
            )
            return Response(200, {
                "link": generated_link
            }).serialize(), 200
        except NameError:
            return Error(500, 'Could not send link to this email').serialize(), 500

    @has_valid_email
    def reset_password(self):
        data = request.json
        email = data['email']
        try:
            generated_link = auth.generate_password_reset_link(
                email=email
            )
            return Response(200, {
                "link": generated_link
            }).serialize(), 200
        except NameError:
            return Error(500, 'Could not send link to this email').serialize(), 500

    @staticmethod
    def get_user():
        try:
            token = request.headers['Authorization']
            claims = auth.verify_id_token(token)
            uid = claims['uid']
            try:
                user = auth.get_user(uid=uid)
                return Response(200, user).serialize(), 200
            except NameError:
                return Error(500, 'Could not get user').serialize(), 500
        except NameError:
            return Error(500, 'Missing UID on token claims').serialize(), 500



