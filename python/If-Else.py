#!/usr/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    r = n % 2
    if r == 0:
        if n in range(2,7):
            print("Not Weird")    
        if n in range(7,21):
            print("Weird")
        if n > 20:
            print("Not Weird")
            
    else:
        print("Weird")


