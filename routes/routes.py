from flask import Blueprint
from .import_export_route import importExport
from .trees_routes import routeTrees
from .greetings import Greetings

Api = Blueprint('back_routes', __name__,)

Api.register_blueprint(importExport, url_prefix='/trees')
Api.register_blueprint(routeTrees, url_prefix='/trees')
Api.register_blueprint( Greetings, url_prefix='/')