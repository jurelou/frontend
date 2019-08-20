from app.api.factory import Factory

factory = Factory()
factory.set_flask()
factory.set_celery()

from api.resources import blueprint as b1

factory.register(b1)