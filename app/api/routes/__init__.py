from flask import Blueprint
from flask_restplus import Api

from app.api.routes.main import api as mainAPI
from app.api.routes.collectors.main import collectors
blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint)

api.add_namespace(mainAPI, path='')
api.add_namespace(collectors, path='')
