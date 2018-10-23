'''
Day - 3
Link : https://www.hackerrank.com/challenges/30-conditional-statements/problem
Problem Statement
Objective
Given an integer, , perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird.
Input Format
A single line containing a positive integer, n .
Constraints
1 <= n <= 100
Output Format
Print Weird if the number is weird; otherwise, print Not Weird.
Sample Input 0
3
Sample Output 0
Weird
Explanation 0
n=3
n is odd and odd numbers are weird, so we print Weird.
Sample Input 1
n=24
Sample Output 1
Not Weird
Explanation 1
n = 24
n >20 and n is even, so it isn't weird. Thus we print not weird.
'''
# Accepted Solution:

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
if (n%2 != 0):
    print("Weird")
elif (2 <= n <= 5 and n%2 == 0):
    print("Not Weird")
elif (6 <= n <= 20 and n%2 == 0):
    print("Weird")
elif ( n%2 == 0 and n > 20):
    print("Not Weird")
