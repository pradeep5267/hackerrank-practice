#%%
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # s and t are the range of the house
    # a is the location of apple tree; b is the location of orange tree
    # apple => distances of apples
    # oranges => distances of oranges
    result_apples = 0
    result_oranges = 0
    '''
    zip doesnt work because zip requires, 
    the array sizes to be same 
    '''
    # THESE WORK
    # for i in apples:
    #     if (s <= a+i <= t):
    #         result_apples += 1
    #         # print(i)
    # for j in oranges:
    #     if (s <= b+j <= t):
    #         result_oranges += 1
    #         # print('oranges: ',j)
    # print(result_apples)
    # print(result_oranges)


    # print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    # print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))
    


s,t = 7, 11

a, b = 5, 15

m, n = 3, 2

apples = [-2, 2]

oranges = [5, -6, -7]

countApplesAndOranges(s, t, a, b, apples, oranges)

#%%
