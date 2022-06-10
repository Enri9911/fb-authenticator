import re
from flask import request
from models.error import Error


def validate(s):
    pat = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(pat, s):
        return True
    return False


def has_valid_email(func):
    def inner(*args, **kwargs):
        email = request.json['email']
        if validate(email):
            return func(*args, **kwargs)
        else:
            return Error(status_code=500, reason='Invalid email').serialize(), 500

    return inner
