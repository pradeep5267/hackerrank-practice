#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        return '26.09.1918'
        
    if (year > 1918 and year%400 == 0 or (year%4 == 0 and year%100 != 0)) or (year <= 1917 and year%4 == 0):
        return f'12.09.{str(year)}'
    else:
        return f'13.09.{str(year)}'
    
#%%
#     13.09.2017 for 2017
#     12.09.2016 for 2016
#     26.09.1918 for 1918
