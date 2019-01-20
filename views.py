import json
import os

from flask import jsonify, Blueprint

from forms import AuthForm

views = Blueprint('views', __name__)

from middleware import *


@views.route('/', methods=['POST'])
def home():
    response = jsonify({'message': 'home'})
    response.status_code = 209
    return response
