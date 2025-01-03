from flask import Flask
from app.routes import main

def create_app():
    """
    Create and configure the Flask application.
    Créer et configurer l'application Flask.

    Returns:
        A configured Flask application instance.
        Une instance de l'application Flask configurée.
    """
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Charger la configuration depuis config.py
    app.register_blueprint(main)  # Enregistrer le blueprint principal pour les routes
    return app

if __name__ == "__main__":
    """
    Entry point for running the Flask application.
    Point d'entrée pour exécuter l'application Flask.
    """
    app = create_app()
    app.run(host="0.0.0.0", port=int(app.config.get("FLASK_PORT", 5000)))
