#!/usr/bin/bash
# Bash script that takes in a URL 
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-