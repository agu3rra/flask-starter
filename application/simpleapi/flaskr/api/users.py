import json
from flask import Response, Blueprint


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