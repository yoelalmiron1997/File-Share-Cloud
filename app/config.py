# app/config.py

import os

class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Carpeta para los archivos subidos
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limitar tamaño del archivo (16 MB)
