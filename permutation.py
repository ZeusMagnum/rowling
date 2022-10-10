#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Write your code here
    if k ==0:
        #When k=0 we just have to print 1 to n 
        return list((range(1,n+1)))
    elif (n/k)%2!=0.0:
        #pattern is not possible when k*2 is not divisible by n
        return [-1]
    else:
        #initialize an empty list
        arr = []
        #create a for loop with k*2 difference, example when k=3 --> 1,7,13,19,25....
        for i in range(1,n,k*2):
            #numbers from i to i+k*2 example when k=3 and i = 1 --> [1,2,3,4,5,6]
            d = list(range(i, i+k*2)) 
            #Slice and interchange left and right part, example [1,2,3,4,5,6] --> [4,5,6,1,2,3]
            arr+=d[k:]+d[:k]
        return (arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
