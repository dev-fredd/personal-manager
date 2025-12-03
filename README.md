# Personal Manager

Proyecto para gestionar tareas personales desarrollado con Flask.

## Instalación

1. Crea un entorno virtual:
```bash
python -m venv venv
```

2. Activa el entorno virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la aplicación:

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## Estructura del Proyecto

```
personal-manager/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── templates/            # Plantillas HTML
│   ├── index.html
│   └── about.html
└── static/               # Archivos estáticos
    └── css/
        └── style.css
```
