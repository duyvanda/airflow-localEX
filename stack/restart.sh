#!/usr/bin/env bash

docker build -t ubuntu:airflow_stack .

docker service rm aiflow_web

docker stack deploy --compose-file docker-compose.yml aiflow