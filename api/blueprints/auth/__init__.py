from quart import Quart, Blueprint

from .middleware import UserMiddleware

blueprint: Blueprint = Blueprint(
    'auth',
    __name__
)


def setup(app: Quart, url_prefix: str):
    from .views import __all__
    # Reguster blueprint to Quart instance.
    app.register_blueprint(
        blueprint=blueprint,
        url_prefix=url_prefix
    )