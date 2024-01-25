# Fast API

## _Creacion de API base con Fast API_

[![N|Solid](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com)

Se crea proyecto base de Fast API con una arquitectura modular y con el uso de conexion con postgresql

## Requerimientos

- [Python](https://www.python.org/downloads/) version 3.9.6
- [PyEnv](https://github.com/pyenv/pyenv#installation)
- [Poetry](https://python-poetry.org/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker compose](https://docs.docker.com/compose/install/)

#### Windows

la instalacion de python en windows, basta con instalar pyenv y seleccionar la version que se requiere
en caso de tener instalado python previamente en windows se debe desinstalar, y hacer la instalacion
con pyenv solo validar que version de python tienen para dejarla de manera predeterminada despues de
crear el ambiente virtual

## Ambiente

Creamos un ambiente virtual con la version de python, con la finalidad de no generar
conflictos entre las versiones de python

```sh
pyenv install 3.9.6

pyenv local 3.9.6
```

Validamos que la version de python sea la que necesitamos

```sh
python --version
```

creamos el ambiente virtual

```sh
python -m venv .venv
```

## Activar el ambiente virtual de python

#### linux / mac

```sh
source ./.venv/bin/activate
```

#### windows power-shell

```sh
.\.venv\Scripts\activate
```

Una vez que la version de python es la correcta y el ambiente virtual esta creado
procedemos a instalar dependencias e iniciar el servidor

```sh
pip install -r requeriments.txt
```

## Iniciar el servidor

Teniendo instalado docker y docker comppose en la raiz del proyecto ejecutamos el siguiente comando para levantar la base de datos

```sh
docker compose up --build
```

una vez iniciada la base de datos prodedemos a levantar el aplicativo

```sh
python server.py
```

si el servidor esta corriendo correctamente podriamos ver
acceder a la siguiente url

### [http://localhost:8432/docs](http://localhost:8432/docs)

Donde podremos ver el listado de los servicios y su forma de consumirlos
