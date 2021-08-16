#!/bin/bash

# activar el virtual environment e iniciar NGINX y uWSGI
source production_venv/bin/activate
sudo /etc/init.d/nginx start
uwsgi --socket mysite.sock --module SAPA.wsgi --chmod-socket=666

# salir del virtual environment y cerrar NGINX
sudo systemctl stop nginx
deactivate

