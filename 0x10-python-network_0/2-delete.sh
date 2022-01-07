#!/usr/bin/env bash
#Delete request
url=$1

curl -X DELETE $url -L
