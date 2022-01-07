#!/usr/bin/env bash
#body size
url=$1
size="$(curl -s $url | wc -c)"
echo "$size"
