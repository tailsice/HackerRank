#!/bin/bash

awk '
    {
        result = 1
        for (i = 1; i < NF; i++) {
            if ($i >= 0 && $i < 50) {
                result = 0;
                break;
            }
        }
        printf("%s : ", $1);
        if (result)
            printf("Pass\n");
        else
            printf("Fail\n");
    }
'

