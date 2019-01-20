from flask import jsonify


def send_json_response(message, status_code):
    response = jsonify(message)
    response.status_code = status_code
    return response
