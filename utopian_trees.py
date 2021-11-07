#%%
n = 5
l = 1

for i in range(n):
    if(i%2 == 0):
        l *= 2
    elif(i%2 == 1):
        l += 1
print(l)

