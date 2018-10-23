#!/bin/python3

import math
import os
import random
import re
import sys

i = int(input())
if 1 <= i <= 1000:
    arr = [int(i) for i in input().split()]

    arr2 = arr[::-1]
    for i in arr2:
        print(i,end=' ')