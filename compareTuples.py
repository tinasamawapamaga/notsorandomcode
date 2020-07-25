#!/bin/python3
"""
compareTriplets has the following parameter(s):
int a[3]: first list values
int b[3]: second list values 
Return
int[2]: first list scores in first pos, second list score in second pos
"""

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    temp=[0,0]
    for x,y in zip(a,b):
        if x>y: temp[0]+=1
        if x<y: temp[1]+=1
    return temp
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
