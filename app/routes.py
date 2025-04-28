from flask import Blueprint, request, send_from_directory, render_template, current_app
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    upload_folder = current_app.config['UPLOAD_FOLDER']
    if request.method == 'POST':
        uploader_name = request.form.get('uploader')  # 👈 Capturamos el nombre
        
        archivos = request.files.getlist('file')
        for archivo in archivos:
            if archivo and archivo.filename:
                # Guardamos el archivo
                save_path = os.path.join(upload_folder, archivo.filename)
                archivo.save(save_path)
                
                # Guardamos el nombre de quien subió
                info_filename = archivo.filename + '.txt'
                info_path = os.path.join(upload_folder, info_filename)
                with open(info_path, 'w') as f:
                    f.write(f"Subido por: {uploader_name}\n")
    archivos_disponibles = os.listdir(upload_folder)
    return render_template('index.html', archivos=archivos_disponibles)

@main.route('/files/<filename>')
def files(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
