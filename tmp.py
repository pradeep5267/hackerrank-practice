#%%
import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    z = n-1
    for i in range(1,n):
        print(' '*z,'#'*i)
        z-=1
    print('#'*n,end='')

staircase(6)


    # z = n-2
    # for i in range(1,n):
    #     print(' '*z, '#'*i)
    #     z-=1
    # print('#'*n)
#%%
#%%
import math
def factors(a, b):
    factor_list = []
    i = 1
    if a > b:
        a, b = b, a
    f_number = a*b
    upper_limit = math.ceil(math.sqrt(f_number))
    while i <= upper_limit:
        if f_number % i == 0:
            tmp = f_number//i
            # if tmp not in factor_list:
            factor_list.append(tmp)
            # if i not in factor_list:
            factor_list.append(i)
        i += 1
    factor_list.remove(1)
    factor_list.sort()
    return factor_list
    # print(factor_list)

def check_sets(arr1, arr2):
    count = 0
    for i in arr2:
        for j in arr1:
            if i%j == 0:
                count += 1
    return count






arr1 = factors(3,5)
count = check_sets(arr1, arr2)


#%%

