#%%
def maximumPerimeterTriangle(sticks):
    flag = 0
    current_max = 0
    sticks.sort()
    for i in range(len(sticks) - 2):
            if (sum(sticks[i:i+2]) > sticks[i+2]):
                current_max = i
                flag += 1
    if flag == 0:
        return [(-1)]
    else:
        return (sticks[current_max:current_max+3])


sticks1 = [1, 1, 1, 3, 3] # 1,1,3
sticks2 = [1, 2, 3] # -1
sticks3 = [1, 1, 1, 2, 3, 5] # 1,1,1

print(maximumPerimeterTriangle(sticks3))

#%%
