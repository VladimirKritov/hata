#!/bin/bash

python3 generator.py

echo '### ###  docker-compose.yml ### ### ###'
echo '### ### ### ### ### ### ### ### ### ###'
cat docker-compose.yml
echo '\n'
echo '### ### ### ### ### ### ### ### ### ###'
echo '\n'

while :
do
  docker-compose up --build --abort-on-container-exit --remove-orphans
  docker-compose down
done
