# Xabi Flask Gunicorn Demo
1. Para ejecutar primero configurar la variable de ambiente:

Para Windows:

Para production
```sh
SET env='production'
```

Para dev
```sh
SET env='development'
```

2. Crear ambiente de trabajo e instalar requirements

Para Windows
```sh
py -m venv env
./env/Scripts/activate.bat
pip install -U pip
pip install -r requirements.txt
```

3. Ejecutar con gunicorn

Nota importante:
- Parametro `-w` es para especificar los trabajadores
Se recomienda 2 * CPUCORES + 1

```sh
gunicorn -w 4 --bind 0.0.0.0:5000 main:app
```
