from flask import Flask

__author__ = 'xing'

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    return app
