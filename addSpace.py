#!/usr/bin/env python
from __future__ import print_function
import sys

with open(sys.argv[1]) as f:
    for line in f:
        for char in line:
            if char.isupper():
               print(char +"|",end="")
            else:
               print(char,end="")
