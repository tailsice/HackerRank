#!/bin/bash

read file
text=${file}
while read file; do
    echo $file >> tmp
done

head -n 21 tmp | tail -n 11
