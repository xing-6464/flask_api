from flask import Flask

__author__ = 'xing'

def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.create_blueprint(create_blueprint_v1(), url_prefix='/api/v1')

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    return app
