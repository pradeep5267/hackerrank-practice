#%%
def divisiblePairs(arr,k):
    count = 0
    print(k,'\n')
    arr = sorted(arr) # not required
    print(arr)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            # print(arr[i]+arr[j])
            if((arr[i]+arr[j])%k == 0):
                print(arr[i],arr[j])
                print('hit')
                count += 1
    print(count)

k = 3
arr = [1,3,2,6,1,2]
divisiblePairs(arr,k)
# %%
