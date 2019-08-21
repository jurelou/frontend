from flask_restplus import Resource
from flask_restplus import Namespace

from app.api.tasks import engineTasks


collectors = Namespace(name='collectors', description='Collectors API namespace.')


@collectors.route('/')
class Collectors(Resource):

    def get(self):

        return {'voila': engineTasks.list_collectors()}


@collectors.route('/<collector_id>')
class Collector(Resource):

    def get(self, collector_id):
        return {'voila': collector_id}
