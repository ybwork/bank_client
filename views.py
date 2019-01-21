import json
import os

from flask import jsonify, Blueprint

from forms import AuthForm

views = Blueprint('views', __name__)

from middleware import *


@views.route('/', methods=['POST'])
def home():
    return send_json_response(
        message={'message': 'home'},
        status_code=200
    )
