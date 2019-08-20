import os
from flask import Flask
from celery import Celery

from app.config import config


class Factory(object):

    def set_flask(self, **kwargs):
        self.flask = Flask(__name__, **kwargs)
        self.flask.config.update(config["flask"])
        return self.flask

    def set_celery(self, **kwargs):
        self.frontend_broker = Celery(config["frontend_broker"]["CELERY_DEFAULT_QUEUE"], **kwargs)
        self.frontend_broker.conf.update(config["frontend_broker"])

        self.engine_broker = Celery(config["backend_broker"]["CELERY_DEFAULT_QUEUE"], **kwargs)
        self.engine_broker.conf.update(config["backend_broker"])

        return (self.frontend_broker, self.engine_broker)

    def register(self, blueprint):
        self.flask.register_blueprint(blueprint)
