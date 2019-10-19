import json
from flask import Response, Blueprint, request


users = [
    {
        "name": "Darth Vader",
        "side": "Sith",
        "power": 5.0
    },
    {
        "name": "Luke Skywalker",
        "side": "Jedi",
        "power": 4.5
    }
]

users_resource = Blueprint('users_resource', __name__)

@users_resource.route('/users')
def get_users():
    response = json.dumps(users)
    return Response(response, status=200, mimetype='application/json')

@users_resource.route('/users', methods=['POST'])
def add_user():
    request_data = request.get_json()
    new_user = {
        "name": request_data.get('name'),
        "side": request_data.get('side'),
        "power": request_data.get('power')
    }
    users.insert(0, new_user)
    response = {
        "status":True,
        "info":"New user created successfully: {}.".format(
            request_data.get('name'))
    }
    return Response(json.dumps(response), status=201, mimetype='application/json')