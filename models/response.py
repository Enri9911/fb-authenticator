from flask import jsonify


class Response:
    def __init__(self, status_code: int, body: object):
        self.status_code = status_code
        self.body = body

    def serialize(self):
        return jsonify({
            "status_code": self.status_code,
            "data": self.body
        })