#! /bin/bash

sleep 10
python3 manage.py makemigrations
python3 manage.py migrate

# # windows

# @echo off
# timeout /t 10 /nobreak >nul
# python manage.py makemigrations
# python manage.py migrate
