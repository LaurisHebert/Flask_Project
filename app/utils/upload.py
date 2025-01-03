# Flask_project/app/utils/upload.py
import pandas as pd

def read_excel(file):
    """
    Read an Excel file and return its data as a DataFrame.
    Lire un fichier Excel et retourner ses données sous forme de DataFrame.

    Args:
        file: The uploaded Excel file.
        Le fichier Excel téléchargé.

    Returns:
        A pandas DataFrame containing the file's data or an error message if the operation fails.
        Un DataFrame pandas contenant les données du fichier ou un message d'erreur si l'opération échoue.
    """
    try:
        data = pd.read_excel(file)
        return data
    except Exception as e:
        return {"error": str(e)}
