#!/bin/bash

docker cp ./data/albumlist.csv Mymongo:/albumlist.csv
docker cp ./scripts/exercise1/exercise1_a.sh Mymongo:/exercise1_a.sh
docker cp ./scripts/exercise1/exercise1_b.js Mymongo:/exercise1_b.js
docker cp ./scripts/exercise1/exercise1_b.sh Mymongo:/exercise1_b.sh
docker cp ./scripts/exercise1/exercise1_c.js Mymongo:/exercise1_c.js
docker cp ./scripts/exercise1/exercise1_c.sh Mymongo:/exercise1_c.sh
docker cp ./scripts/exercise1/exercise1_d.js Mymongo:/exercise1_d.js
docker cp ./scripts/exercise1/exercise1_d.sh Mymongo:/exercise1_d.sh