'''
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. 
Print the decimal value of each fraction on a new line.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_pos, count_neg, count_zero = 0, 0, 0
    for num in arr:
        if (num > 0):
            count_pos += 1
        elif (num < 0):
            count_neg += 1
        elif (num == 0):
            count_zero += 1
    arr_len = float(len(arr))
    print(float(count_pos/arr_len))
    print(float(count_neg/arr_len))
    print(float(count_zero/arr_len))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
