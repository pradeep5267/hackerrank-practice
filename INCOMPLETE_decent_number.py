#%%
from collections import Counter
def decentNumber(n):
    '''
    Have not wrapped my head arounf this
    explanation as stated: 
    I am presenting two solutions. The naive brute force solution executes in 
    O(N) and passes all the tests. Yet further optimisations and a runtime complexity of 
    O(1) are possible.

    When observing the possible output space we realise that there 
    can only be 0, 5 or 10 threes in the output. If there would be 15 threes, 
    it is better to use fives instead. The number of trailing threes can 
    therefore be defined by K = 5*((2*N)%3). 
    Let us plug some numbers into the equation:

    1 -> 5*(2%3) = 10 -> INVALID
    2 -> 5*(4%3) = 5 -> INVALID
    3 -> 5*(3%3) = 0 -> 555
    4 -> 5*(8%3) = 10 -> INVALID
    5 -> 5*(10%3) = 5 -> 33-33-3
    8 -> 5*(16%3) = 5 -> 555-33-33-3
    10 -> 5*(20%3) = 10 -> 33-33-33-33-33
    15 -> 5*(30%3) = 0 -> 555-555-555-555-555


    '''
    c = 5*(2*n%3)
    if c > n:
        print (-1)
    else:
        print ('5' * (n-c) + '3'*c)
#%%
def sherlockBeastNaive(N):
    if (N < 3): 
        return "-1" 
    three_cnt = N//3 
    five_cnt = 0 
    while three_cnt >=0:
        rem = N - three_cnt*3
        if rem % 5 == 0:
            five_cnt = rem/5
            break
        three_cnt -= 1
         
    if three_cnt <= 0 and five_cnt == 0:
        return "-1"
     
    return "555"*three_cnt + "33333"*five_cnt