#!/bin/bash

. settings.ini

#Installation du virtual env
echo "Installation du virtual env..."
virtualenv venv

if [[ $python_path ]]; then
  virtualenv -p $python_path venv
fi

source venv/bin/activate
pip install -r requirements.txt
deactivate
