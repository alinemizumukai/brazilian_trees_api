from flask import Blueprint
from .root_route import RootRoute
from .trees_routes import routeTrees
from .greetings import Greetings

Api = Blueprint('back_routes', __name__,)

Api.register_blueprint(RootRoute, url_prefix='/root')
Api.register_blueprint(routeTrees, url_prefix='/trees')
Api.register_blueprint( Greetings, url_prefix='/')