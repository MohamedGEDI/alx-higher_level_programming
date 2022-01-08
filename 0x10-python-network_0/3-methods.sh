#!/bin/bash 
#Get request
curl -s -X get $1 -I | head -n 3 | tail -1 | cut -b 8-
