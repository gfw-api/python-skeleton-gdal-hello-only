"""API ROUTER"""
from flask import jsonify, Blueprint

endpoints = Blueprint('endpoints', __name__)


@endpoints.route('/loadtest-python', strict_slashes=False, methods=['GET'])
def say_hello():
    return jsonify({"response": "ok"}), 200
