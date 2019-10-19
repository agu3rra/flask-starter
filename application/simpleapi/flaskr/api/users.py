import json
from flask import Response


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

def get_users():
    response = json.dumps(users)
    return Response(response, status=200, mimetype='application/json')