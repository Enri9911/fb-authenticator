import re
from flask import request
from models.error import Error


def validate(s):
    pat = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
    if re.fullmatch(pat, s):
        return True
    return False


def has_valid_password(func):
    def inner(*args, **kwargs):
        email = request.json['password']
        if validate(email):
            return func(*args, **kwargs)
        else:
            return Error(status_code=500, reason='Invalid password').serialize(), 500

    return inner
