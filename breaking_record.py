#%%
import sys
import math


def breakingRecords(scores):
    '''
    the sys.maxsize gives the maximum interger value that an 
    int can hold
    '''
    min_holder = sys.maxsize
    max_holder = -(sys.maxsize)
    min_counter, max_counter = -1, -1
    for i in scores:
        if i < 0:
            return -1
        if (i < min_holder):
            min_counter += 1
            min_holder = i
        if (i > max_holder):
            max_counter += 1
            max_holder = i
    # final_count = (min_counter-1) + max_counter
    return (max_counter,min_counter)



scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
print(record_counter(scores))

#%%
