#!/bin/bash

# Get the year from the first command-line argument
year="$1"

# Check if the year was provided
if [ -z "$year" ]; then
  echo "Gib year!!!!"
  echo "Usage: ./boom.sh <year>"
  exit 1
fi

# Create the year directory if it doesn't exist
mkdir -p "$year"

for i in {1..25}; do
  mkdir "$year/d$i"
  cp sol.py "$year/d$i/sol.py"
  touch "$year/d$i/f.in" "$year/d$i/f_test.in"
done