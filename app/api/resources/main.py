from time import sleep
from flask_restplus import Resource, Namespace
from celery.utils.log import get_task_logger

from app.api import factory

from app.api.tasks import frontendtasks


api = Namespace(name='', description='Main API namespace.')
logger = get_task_logger(__name__)
celery = factory.frontend_broker


@api.route('/hello/<name>')
@api.doc(params={'name': 'The name of the person to return hello.'})
class HelloWorld(Resource):
    """HelloWorld resource class."""

    def get(self, name):
        """Get method."""
        return {'hello': name}


@api.route('/bye/<name>')
@api.doc(params={'name': 'The name of the person to return bye.'})
class ByeWorld(Resource):
    """ByeWorld resource class."""

    def get(self, name):
        """Get method."""
        frontendtasks.toto()

        self.asynchronous.apply_async((name,))
        return {'bye': name}

    @celery.task(bind=True)
    def asynchronous(self, name):
        """Async long task method."""
        sleep(1)
        """
        self.update_state(state='PROGRESS',
                          meta={'current': "i", 'total': "total",
                                'status': "message"})        
        """
        return {'async': name}
