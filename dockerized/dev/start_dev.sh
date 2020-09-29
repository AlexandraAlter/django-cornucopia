#!/bin/sh

/opt/wait-for-it/wait-for-it.sh db:5432

django-admin migrate
django-admin createsuperuser_dev
django-admin runserver 0.0.0.0:8000
