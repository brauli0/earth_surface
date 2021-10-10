#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: create-project.sh [name]"
    exit 1
fi

echo Cloning project...
git clone https://github.com/brauli0/python-server-skeleton.git
echo
echo Setting name...
mv python-server-skeleton $1
cd $1
echo
echo Removing git...
rm -rf .git
echo DONE