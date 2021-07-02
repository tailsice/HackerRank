#!/bin/bash

read file
text=${file}
while read file; do
    text="${text}\n${file}"
done
printf "${text}" | head -c 20

