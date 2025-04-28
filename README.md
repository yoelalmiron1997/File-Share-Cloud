## File Share Cloud

Es un proyecto que crea un servidor local intermedio como respaldo, facilitando el intercambio de archivos entre dos computadoras dentro de la misma red.

```yaml
file-share-cloud/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── styles.css
│
├── uploads/ # Carpeta donde se guardan los archivos subidos
│
├── requirements.txt
├── run.py
└── README.md
```

# Características

- **Subida de Archivos**: Los usuarios pueden subir múltiples archivos a través de una interfaz web sencilla.
- **Visualización de Archivos**: Los archivos subidos se muestran en la misma página, con enlaces para descargarlos.
- **Compatible con Redes Locales**: Ideal para compartir archivos entre computadoras en la misma red local sin necesidad de servicios de terceros.

# Requisitos

- **Python**: 3.6 o superior
- **Sistema operativo**: Compatible con Linux y Windows
- **Dependencias**: Flask (y otras dependencias listadas en `requirements.txt`)

# Instalación

## Clonar el repositorio

Si aún no tienes el repositorio, puedes clonarlo utilizando Git:

```bash
git clone https://github.com/tu-usuario/file-share-cloud.git
```

# Instalar las dependencias

Navega al directorio del proyecto e instala las dependencias utilizando pip:

```bash
cd file-share-cloud
pip install -r requirements.txt
```

# Configurar el servidor local

El archivo config.py contiene la configuración para las rutas y los parámetros del servidor (como el directorio de subida de archivos).
Puedes personalizar estos valores según sea necesario.

# Ejecutar el servidor

Una vez que las dependencias estén instaladas, puedes iniciar el servidor con el siguiente comando:

```bash
python run.py
```

El servidor se ejecutará en http://127.0.0.1:5000/ de manera predeterminada.

# Uso

## Acceder a la aplicación

Abre tu navegador y navega a:

```bash
http://127.0.0.1:5000/
```

## Subir archivos

Usa el formulario de la página principal para seleccionar y subir archivos desde tu computadora.
Los archivos seleccionados se cargarán al servidor y podrás verlos en la lista de archivos disponibles.

## Descargar archivos

Los archivos subidos se mostrarán en una lista con enlaces que permiten descargarlos directamente.

## Archivos Subidos

Los archivos subidos por los usuarios se almacenan en la carpeta uploads/.
Cada archivo se guarda con su nombre original, y un archivo de texto relacionado almacena información sobre el usuario que subió el archivo (si se configura en la aplicación).

# Compatibilidad de Sistemas Operativos

File Share Cloud es compatible con sistemas operativos Linux y Windows.

# Licencia

Este proyecto es de código abierto y está disponible bajo los términos de la licencia MIT.

© 2025 Yoel Maximiliano Almirón. Todos los derechos reservados.
