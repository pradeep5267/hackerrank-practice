#%%
def toys(arr1):
    arr1.sort()
    currnet_min = arr1[0]
    contaier_count = 1
    for i in arr1:
        if i > currnet_min+4:
            contaier_count += 1
            currnet_min = i
    print (contaier_count)


arr1 = '12 15 7 8 19 24'
# arr1 = '1 2 3 21 7 12 14 21'
arr1 = list(arr1.split(' '))
arr1 = [int(i) for i in arr1]
toys(arr1)
# %%
