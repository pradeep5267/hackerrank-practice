#%%
import math
import os
import random
import re
import sys

# Complete the staircase function below.
# COMMA INTRODUCES A SPACE AUTOMATICALLY !!!

def staircase(n):
    for i in range(1, n):
        print(' '*(n-i-1),'#'*i)
    print('#'*n)
staircase(6)


# OR TO AVOID THE SPACING ISSUES INTRODUCED DUE TO COMMA IN PRINT
    # for i in range(1, n):
    #     print(' '*(n-i),end='')
    #     print('#'*i)
    # print('#'*n)

#%%
