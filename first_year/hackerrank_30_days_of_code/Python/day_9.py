'''
Day - 8
Link : https://www.hackerrank.com/challenges/30-recursion/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
# Complete the factorial function below.
def factorial(n):
    if n<=1:
        return 1

    return n*factorial(n-1)

def factorial_functional(n):
    return reduce(lambda x,y:x*y,range(1,n+1))

def main():
    n = int(input())
    print(factorial(n))

if __name__ == "__main__":
    main()
