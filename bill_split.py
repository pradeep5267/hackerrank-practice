#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    full_bill_sum = sum(bill)
    part_bill_sum = full_bill_sum-bill[k]
    j = int(part_bill_sum/2)
    if j == b:
        print('Bon Appetit')
    else:
        print(b-j)

k = 1

bill = [3, 10, 2, 9]

b = 12
bonAppetit(bill, k, b)
