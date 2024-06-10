#!/bin/bash

mongoimport --db musicDB --collection albums --type csv --headerline --file albumlist.csv