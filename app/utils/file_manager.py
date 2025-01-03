import os
from werkzeug.utils import secure_filename
from fpdf import FPDF
from datetime import datetime

def save_uploaded_file(upload_folder, file):
    """
    Sauvegarde un fichier téléchargé dans le dossier spécifié.

    Args:
        upload_folder (str): Dossier où sauvegarder le fichier.
        file (werkzeug.datastructures.FileStorage): Fichier téléchargé.

    Returns:
        str: Chemin du fichier sauvegardé.
    """
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, secure_filename(file.filename))
    file.save(file_path)
    return file_path

def generate_pdf(data, pdf_folder, template_type):
    """
    Génère un fichier PDF basé sur un type de modèle.

    Args:
        data (dict): Données pour remplir le modèle.
        pdf_folder (str): Dossier où sauvegarder les PDFs.
        template_type (str): Type de modèle (ex: "A", "B").

    Returns:
        str: Chemin du fichier PDF généré.
    """
    templates = {
        "A": "templates/fiche_A.txt",
        "B": "templates/fiche_B.txt"
    }

    if template_type not in templates:
        raise ValueError("Invalid template type")

    template_path = templates[template_type]
    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()

    today = datetime.now().strftime("%d/%m/%Y")
    filled_text = template.replace("[Date]", today)
    for key, value in data.items():
        filled_text = filled_text.replace(f"[{key}]", str(value))

    os.makedirs(pdf_folder, exist_ok=True)
    pdf_file_path = os.path.join(pdf_folder, f"{data['Nom']}_{data['Prénom']}_{template_type}.pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in filled_text.split("\n"):
        pdf.cell(0, 10, txt=line, ln=True)

    pdf.output(pdf_file_path)
    return pdf_file_path
