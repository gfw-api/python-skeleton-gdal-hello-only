"""API ROUTER"""

import logging

from flask import jsonify, Blueprint
import json

psone_endpoints = Blueprint('psone_endpoints', __name__)


@psone_endpoints.route('/dissolve', strict_slashes=False, methods=['POST'])
def say_hello():
    """World Endpoint"""
    logging.info('[ROUTER]: starting dissolve')

    return jsonify({"dissolve": "ok"}), 200
