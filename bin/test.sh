#!/bin/bash

response=$(curl -s http://localhost:80/helloworld)
if [ "$response" == "\"Hello world!\"" ]; then
    echo "It WORKS!"
else
    echo "It DOESN'T work"
fi