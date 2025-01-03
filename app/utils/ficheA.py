# Exemple de définition de create_fiche_A
from fpdf import FPDF


def create_fiche_A(data, output_path=None):
    """
    Génère un fichier PDF à partir des données fournies.

    Args:
        data (dict): Les données à inclure dans le PDF.
        output_path (str): Chemin de sortie pour le fichier PDF.

    Returns:
        str: Chemin du fichier PDF généré.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Ajouter des données dans le PDF
    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    if output_path:
        pdf.output(output_path)  # Sauvegarde dans le chemin spécifié
    else:
        pdf.output(f"{data['Nom']}_{data['Prénom']}.pdf")  # Sauvegarde dans le répertoire courant

    return output_path or f"{data['Nom']}_{data['Prénom']}.pdf"
