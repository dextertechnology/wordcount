#!/bin/bash

# run this script to start wordcount
# server only for the first time

if [[ "$VIRTUAL_ENV" != "" ]]
then
  echo "Alreaady inside virtual environment. Deactivate first to continue.";
  return
else
  python -m venv wordcount-venv
  source wordcount-venv/bin/activate

  pip install --upgrade pip
  pip install -r requirements.txt

  python manage.py collectstatic
  python manage.py runserver
fi