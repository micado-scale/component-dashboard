import os

from logging.config import dictConfig
from flask import Flask, redirect
from flask_menu import Menu

from .views.home import home

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
Menu(app=app)

def init_application(app):
    app.config["TESTING"] = False
    app.config["DEBUG"] =  False
    app.config["FRONTEND_IP"] = os.getenv(
        'MICADO_FRONTEND_IP', '127.0.0.1')
    app.config["MICADO_VERSION"] = os.getenv(
        'MICADO_VERSION', '------')
    app.config["DISABLE_OPTIMIZER"] = os.getenv(
        'DISABLE_OPTIMIZER', 'FALSE')
    app.config["ENABLE_OCCOPUS"] = os.getenv(
        'ENABLE_OCCOPUS', 'FALSE')
    app.register_blueprint(home)
    app.logger.info("{} application initialized using frontend IP {}" \
        .format(__name__, app.config["FRONTEND_IP"]))

init_application(app)
