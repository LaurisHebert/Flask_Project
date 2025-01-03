from flask import request, jsonify

def validate_file(allowed_extensions):
    """
    Middleware pour valider les fichiers téléchargés.

    Args:
        allowed_extensions (tuple): Extensions de fichier acceptées.

    Returns:
        func: Fonction décoratrice pour la validation.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if 'file' not in request.files:
                return jsonify({"error": "No file uploaded."}), 400

            file = request.files['file']
            if file.filename == '':
                return jsonify({"error": "Empty file name."}), 400

            if not file.filename.endswith(allowed_extensions):
                return jsonify({"error": f"Invalid file type. Allowed: {allowed_extensions}"}), 400

            return func(file, *args, **kwargs)  # Passe le fichier à la fonction suivante
        return wrapper
    return decorator
