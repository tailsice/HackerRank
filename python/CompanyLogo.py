#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    s = sorted(s)
    
    ans = Counter(list(s))
    
    for k,v in ans.most_common(3):
        print(k,v)

