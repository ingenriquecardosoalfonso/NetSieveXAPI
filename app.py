import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request
from flask_cors import CORS
from config import Config
from extensions import db
from flasgger import Swagger
from routes.auth_routes import auth_bp
from routes.users_routes import users_bp
from routes.metrics_routes import metrics_bp
from routes.networkflows_routes import network_flow_bp
from routes.ml_routes import ml_bp

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)

CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:5173",
            "https://localhost:5173",
            "https://delightful-coast-00b044310.7.azurestaticapps.net"
        ],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})


@app.after_request
def after_request(response):
    origin = request.headers.get("Origin")

    allowed_origins = [
        "http://localhost:5173",
        "https://localhost:5173",
        "https://delightful-coast-00b044310.7.azurestaticapps.net"
    ]

    if origin in allowed_origins:
        response.headers["Access-Control-Allow-Origin"] = origin

    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Credentials"] = "true"

    return response


@app.route('/api/<path:path>', methods=['OPTIONS'])
def handle_options(path):
    return '', 200

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "title": "NetSieveX API",
    "version": "0.0.1",
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Ingresa tu token así: **Bearer <token>**"
        }
    },
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "NetSieveX API",
        "version": "0.0.1",
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Ingresa tu token así: Bearer <token>"
        }
    },
    "security": [{"Bearer": []}]
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)


db.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(users_bp, url_prefix="/api")
app.register_blueprint(metrics_bp, url_prefix="/api")
app.register_blueprint(network_flow_bp, url_prefix="/api")
app.register_blueprint(ml_bp, url_prefix="/api")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)