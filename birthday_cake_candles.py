#%%
import math
import os
import random
import re
import sys
'''
For example, if your niece is turning  years old, 
and the cake will have  candles of height 4, 1, 3, 4, she 
will be able to blow out 2 candles successfully, since the 
tallest candle is of height 4 and there are 2 such candles.
'''
def birthdayCakeCandles(ar):
    #### technically required approach
    large = 0
    for i in ar:
        if(i>large):
            large = i
            counter = 1
        elif (large == i):
            counter+=1
    return counter

    #### Pythonic approach
    # return ar.count(max(ar))

    #### My approach
    # large = 0
    # counter = 0
    # for i in ar:
    #     if (i > large):
    #         large = i
    # for i in range(0,len(ar)):
    #     if (ar[i] == large):
    #         counter+= 1
    # return counter

  

 


ar = [1,5,3,1,2,5,5]
result = birthdayCakeCandles(ar)
print(result)

#%%
