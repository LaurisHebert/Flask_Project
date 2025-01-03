
from app.translations import get_translation
from flask import Blueprint, jsonify, render_template, current_app
from app.utils.file_manager import save_uploaded_file, generate_pdf
from app.middlewares import validate_file
from app.utils.upload import read_excel

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Affiche la page d'accueil.

    Returns:
        Une page HTML rendue pour la page d'accueil.
    """
    return render_template('index.html', get_translation=get_translation)

@main.route('/upload', methods=['GET','POST'])
@validate_file(allowed_extensions=('.xls', '.xlsx'))
def upload_page(file):
    """
    Gère l'upload d'un fichier et génère des PDFs.

    Args:
        file: Fichier téléchargé validé.

    Returns:
        JSON avec les informations sur les PDFs générés.
    """
    # Sauvegarder le fichier
    download_folder = current_app.config['DOWNLOAD_FOLDER']
    file_path = save_uploaded_file(download_folder, file)

    # Lire le fichier Excel
    data = read_excel(file_path)
    if "error" in data:
        return jsonify({"error": data["error"]}), 500

    # Générer les PDFs
    pdf_folder = current_app.config['PDF_FOLDER']
    pdf_files = []
    for _, row in data.iterrows():
        pdf_path = generate_pdf(row.to_dict(), pdf_folder, template_type="A")
        pdf_files.append(pdf_path)

    return jsonify({"message": "PDFs created", "files": pdf_files})
