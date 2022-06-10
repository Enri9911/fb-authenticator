from flask import jsonify


class Error:
    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.reason = reason

    def serialize(self):
        return jsonify({
            "status_code": self.status_code,
            "reason": self.reason
        })
