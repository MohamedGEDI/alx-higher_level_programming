#!/usr/bin/env bash
#body size
url=$1
curl -s $url | wc -c
