#!/bin/bash

echo Creating environment...
python3 -m venv env
echo
echo Activating environment...
source env/bin/activate
echo
echo Installing requirements...
pip3 install -r requirements.txt
echo
echo Running server...
chmod 774 bin/test.sh
python3 src/server.py
chmod 774 bin/clean.sh
bin/clean.sh
echo DONE