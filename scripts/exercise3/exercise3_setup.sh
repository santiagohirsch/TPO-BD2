#!/bin/bash

docker cp ./data/bataxi.csv Myredis:/bataxi.csv
docker cp ./scripts/exercise3/exercise3.py Myredis:exercise3.py