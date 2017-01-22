#!/bin/bash

# script to kill all instances, remove also data containers
echo "WARNING! This will kill all containers, and also permanently delete"
echo "all data volumes and the data within them! Are you sure you want to"
echo "continue? [CTRL+C to exit, enter to continue]"
read

docker-compose down -v
docker volume rm 
