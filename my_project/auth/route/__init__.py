"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    # from .orders.client_route import client_bp
    # from .orders.client_type_route import client_type_bp
    from .orders.agencies_route import agencies_bp
    from .orders.animator_route import animator_bp 
    from .orders.event_route import event_bp
    from .orders.event_type_route import event_type_bp
    from .orders.animator_agency_route import animator_agency_bp

    # app.register_blueprint(client_bp)
    # app.register_blueprint(client_type_bp)
    app.register_blueprint(agencies_bp)
    app.register_blueprint(animator_bp)
    app.register_blueprint(event_bp)
    app.register_blueprint(event_type_bp)
    app.register_blueprint(animator_agency_bp)
