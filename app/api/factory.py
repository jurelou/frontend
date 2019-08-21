import os
from flask import Flask
from kombu import Queue
from kombu import Exchange
from celery import Celery

from app.config import config


class Factory(object):

    def set_flask(self, **kwargs):
        self.flask = Flask(__name__, **kwargs)
        self.flask.config.update(config["flask"])
        return self.flask

    def _config_celery(self, config, **kwargs):
        task_queues = {"task_queues" : (
            Queue(
                config["name"],
                Exchange(config["name"]),
                routing_key=config["name"]
            ),
        )}
        app = Celery(config["name"], **kwargs)
        app.conf.update(config)
        app.conf.update(task_queues)
        return app

    def set_celery(self, **kwargs):
        self.frontend_app = self._config_celery(config["frontend_app"], **kwargs)
        self.engine_app = self._config_celery(config["engine_app"], **kwargs)
        self.scan_app = self._config_celery(config["scan_app"], **kwargs)

    def register(self, blueprint):
        self.flask.register_blueprint(blueprint)
