from app.api.factory import Factory

factory = Factory()
factory.set_flask()
factory.set_celery()

from app.api.routes import blueprint as b1

factory.register(b1)