import importlib

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.inc import ResponseException
from werkzeug.exceptions import HTTPException


def handler_error(app):
    

    @app.errorhandler(HTTPException)
    def handler_error(error):
        return ResponseException(error.name, status=error.code).to_dict(), error.code


    @app.errorhandler(ResponseException)
    def handler_error(error):
        response = error.to_dict()
        return response, response['status']


    @app.errorhandler(Exception)
    def handler_error(error):
        data = str(error) if app.config['DEBUG'] else None
        return ResponseException(data, status=500).to_dict(), 500

app = Flask(__name__, instance_relative_config=True)
handler_error(app)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

modules = [
    {'name': 'info', 'path': '/info', 'version': 1},
]

for item in modules:
    module = importlib.import_module(f".{item['name']}", package="app.api")
    app.register_blueprint(
        getattr(module, f"{item['name']}"),
        url_prefix=f"/api/v{item['version']}{item['path']}"
    )
