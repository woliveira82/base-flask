import importlib

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
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
