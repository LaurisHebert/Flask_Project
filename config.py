import os

class Config:
    """
    Configuration class for the Flask application.
    Classe de configuration pour l'application Flask.

    Contains settings for database, secret key, and file paths.
    Contient les paramètres pour la base de données, la clé secrète et les chemins de fichiers.
    """
    DATABASE_URL = f"postgresql://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
    # URL de connexion à la base de données PostgreSQL, construite à partir des variables d'environnement.

    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    # Clé secrète utilisée pour la sécurité de Flask (sessions, cookies, etc.).

    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './uploads')
    # Chemin du dossier où les fichiers téléchargés seront stockés.

    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')
    # Active le mode debug selon l'environnement (défaut : désactivé en production).