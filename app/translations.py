# Flask_project/app/translations.py
from flask import session


# Dictionnaire contenant les traductions pour le texte affiché dans l'application
# Dictionary containing translations for the text displayed in the application
translations = {
    "fr": {
        # Global
        "app_name": "Liriscom generateur de pdf",
        "new_pdf" : "Nouveau PDF",
        "nav_upload": "Téléchargement",
        "title": "Télécharger un fichier Excel",
        "heading": "Téléchargez un fichier Excel",
        "choose_file": "Choisissez un fichier Excel :",
        "upload_button": "Téléverser",
        "welcome_title": "Bienvenue dans le générateur de PDF",
        "welcome_message": "Téléchargez un fichier Excel pour générer des documents PDF.",
        "error_no_file": "Aucun fichier téléchargé.",
        "error_empty_file": "Nom de fichier vide.",
        "change_language": "Changer de langue",

        # Page-specific
        "index_heading": "Bienvenue sur la page d'accueil",
        "index_description": "Ceci est la page d'accueil de notre application. Utilisez la barre de navigation pour explorer.",

        "upload_heading": "Téléchargez votre fichier",
        "upload_description": "Utilisez cette page pour télécharger vos fichiers Excel à traiter.",

        "footer_text": "© 2025 Mon App - Tous droits réservés.",
    },
    "en": {
        # Global
        "app_name": "Liriscom PDF Generator",
        "new_pdf": "New PDF",
        "nav_upload": "Upload",
        "title": "Upload an Excel File",
        "heading": "Upload an Excel File",
        "choose_file": "Choose an Excel file:",
        "upload_button": "Upload",
        "welcome_title": "Welcome to the PDF Generator",
        "welcome_message": "Upload an Excel file to generate PDF documents.",
        "error_no_file": "No file uploaded.",
        "error_empty_file": "Empty file name.",
        "change_language": "Change language",

        # Page-specific
        "index_heading": "Welcome to the Home Page",
        "index_description": "This is the homepage of our application. Use the navigation bar to explore.",

        "upload_heading": "Upload Your File",
        "upload_description": "Use this page to upload your Excel files for processing.",

        "footer_text": "© 2025 My App - All rights reserved.",
    }
}

def get_translation(key):
    """
    Fonction utilitaire pour récupérer les traductions.

    Args:
        key (str): La clé pour le texte à traduire.

    Returns:
        str: Le texte traduit ou la clé si elle est introuvable.
    """
    # Récupérer la langue de la session (par défaut 'en' si elle n'est pas définie)
    lang = session.get('lang', 'en')
    return translations.get(lang, {}).get(key, key)