#!/bin/bash
# This script takes a URL as an argument

curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r\n'
