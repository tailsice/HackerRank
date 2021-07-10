#!/bin/bash

read N
if (( $N == 1 )); then 
    echo $N
else
    LIST=($(cat))
    LIST=${LIST[*]}
    echo $((${LIST// /^}))
fi
