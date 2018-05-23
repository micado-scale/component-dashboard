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

def init_application(app, config):
    app.config.from_object(config)
    app.register_blueprint(home)
    app.logger.info("{} application initialized".format(__name__))
