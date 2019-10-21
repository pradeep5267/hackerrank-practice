#%%
def getMinimumCost5(k,c):
    c.sort(reverse=True)
    n = len(c)
    purchase_counter = [1]*(k)
    print(purchase_counter)
    print(c)
    i, j, cost, purchase_tracker = 0, 0, 0, 0
    tmp = 0
    for i in range (0,n):
        print(f"i {i} j {j} cost {tmp} purchase tracker {purchase_tracker} at {i}")
        tmp = tmp + c[i]*(purchase_tracker + 1)
        if j == k-1:
            j = 0
            purchase_tracker += 1
        else:
            j += 1 
    print(tmp)

k = 3
c = [1, 3, 5, 7, 9] # len of c = n
getMinimumCost5(k,c)
