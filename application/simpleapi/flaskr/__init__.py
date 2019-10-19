import os
import json
from flask import Flask, Response
from . import api

def create_app(test_config=None):
    # Create and configure the app (Factory Function)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config you were given
        app.config.from_mapping(test_config)

    # Ensure my instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # My status response
    @app.route('/')
    def status():
        response = {
            "status":True,
            "info":"I am alive!"
        }
        response = json.dumps(response)
        return Response(response, status=200, mimetype='application/json')

    @app.route('/users')
    def get_users():
        return api.get_users() 

    return app