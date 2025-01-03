# Flask_project/app/__init__.py
from flask import Flask
from app.routes import main

def create_app():
    """
    Create and configure the Flask application.

    Returns:
        A configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configuration from config.py
    app.register_blueprint(main)  # Register the main blueprint for routes
    return app
