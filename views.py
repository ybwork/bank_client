import os

from flask import jsonify, Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    response = jsonify({'message': os.urandom(16).hex()})
    response.status_code = 200
    return response
