#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    total = 1
    for x in s:
        if x.isupper():
            total +=1

    return total

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "saveChangesInTheEditor" #input()

    result = camelcase(s)

    #fptr.write(str(result) + '\n')

    #fptr.close()
