#%%
def largest_permutation(k, arr):
    print(arr)
    n = len(arr)
    max_value = 0
    max_index = 0
    z = 0

    while(k > 0):
        for j in range(z, n):
            if (arr[j] > max_value):
                max_value = arr[j]
                max_index = j
        arr[z], arr[max_index] = arr[max_index], arr[z]
        z += 1
        k -= 1
    print(arr)

k = 1
arr1 = '2 1 3'

# k = 1
# arr1 = '4 2 3 5 1'

arr1 = list(arr1.split(' '))
arr1 = [int(i) for i in arr1]

largest_permutation(k, arr1)
# %%
