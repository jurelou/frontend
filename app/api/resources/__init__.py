from flask import Blueprint
from flask_restplus import Api

from app.api.resources.main import api as main

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint)

api.add_namespace(main, path='')
