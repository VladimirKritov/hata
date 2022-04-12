#!/bin/bash

python3 generator.py
cat docker-compose.yml
echo '\n'

while :
do
  docker-compose up --build --abort-on-container-exit --remove-orphans
  docker-compose down
done
