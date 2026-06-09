# Backend (Django)

Instrucciones rápidas para crear el entorno virtual e instalar dependencias:

```bash
# Crear y activar venv
python3 -m venv venv
source venv/bin/activate

# Actualizar pip e instalar dependencias
pip install --upgrade pip
pip install -r ../requirements.txt

# Crear las migraciones y aplicar (si usas djongo/mongodb puede variar)
python manage.py makemigrations
python manage.py migrate

# Ejecutar servidor de desarrollo
python manage.py runserver
```

Todo el código de la aplicación Django está en el paquete `octofit_tracker`.
