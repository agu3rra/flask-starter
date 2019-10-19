import os
import json
from flask import Flask, Response
import routes


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

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
        "info":"Hello! I am alive!"
    }
    response = json.dumps(response)
    return Response(response, status=200, mimetype='application/json')

app.register_blueprint(routes.users_resource, url_prefix='/api')