#!/bin/sh

django-admin migrate
django-admin runserver 0.0.0.0:8000
