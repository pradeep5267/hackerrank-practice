#!/bin/python3
#%%
import math
import os
import random
import re
import sys

'''
Here the one has to calculate the largest and
smallest sum of an array by summing 4 of 5 integers
hence calculating the sum of array, then subtracting the 
smallest element will give the largest sum, whereas subtracting 
the largest element will give the smallest sum
'''

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    # sum_arr = []
    # for i in range(0,len(arr)):
    #     # print(i)
    #     tmp = sum(arr) - arr[i]
    #     sum_arr.append(tmp)
    # sum_arr.sort()
    # print(sum_arr[0],sum_arr[-1])

    # OR
    min_sum = 10000000
    max_sum = 0
    tmp = 0
    for i in arr:
        tmp = tmp + i
        if(i<min_sum):
            min_sum = i
        if(i>max_sum):
            max_sum = i
    print((tmp-max_sum),(tmp-min_sum))
        


arr = [1,5,7,3,9]
miniMaxSum(arr)


#%%
