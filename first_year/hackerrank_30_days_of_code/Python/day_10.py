'''
Day - 10
Link : https://www.hackerrank.com/challenges/30-binary-numbers/problem
'''

#  Accepted Solution

# Collections - This module implements specialized container datatypes providing alternatives to Python’s
# general purpose built-in containers, dict, list, set, and tuple.
from collections import deque # deque : list-like container with fast appends and pops on either end.

def to_binary(n):
    # To convert a decimal number to a binary string.
    d = deque()
    while n>0:
        d.appendleft(n % 2)
        n = n // 2
    return ''.join(map(str, d))

def count_consecutive(string, target_ch):
    # Count the max consecutive character occurences in the string.
    count = 0
    max_count = 0
    for ch in string:
        if ch == target_ch:
            count += 1
        elif count > 0:
            max_count = max(count, max_count)
            count = 0
    max_count = max(count, max_count)
    return max_count

def main():
    n = int(input())
    print(count_consecutive(to_binary(n),"1"))
