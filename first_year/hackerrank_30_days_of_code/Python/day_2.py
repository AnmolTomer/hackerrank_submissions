'''
Day - 2
Link : https://www.hackerrank.com/challenges/30-operators/problem?h_r=next-challenge&h_v=zen

Problem Statement
Objective
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Input Format

There are 3 lines of numeric input:
The first line has a double, mealCost  (the cost of the meal before tax and tip).
The second line has an integer, tipPercent (the percentage of mealCost being added as tip).
The third line has an integer, totalCost (the percentage of mealCost being added as tax).

Output Format

Print the total meal cost, where  is the rounded integer result of the entire bill ( with added tax and tip).

Sample Input

12.00
20
8
Sample Output

15
'''
# Accepted Solution: 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def bill(meal_cost, tip_percent, tax_percent):
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    tip = meal_cost*tip_percent/100
    tax = meal_cost*tax_percent/100
    total = meal_cost+tip+tax
    round_total = round(total)
    print(round_total)

bill(12,8,20)
