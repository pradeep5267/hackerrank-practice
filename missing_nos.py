#%%
# def missingNumbers(arr, brr):
#     arr1 = list(range(0,1000))
#     for i in arr:
#         arr1[i] = 0
#     for i in brr:
#         arr1[i]-=1
#     for i in arr1:
#         if (i<=0):
#             print(i,(abs(i)))
#     print(arr1)
# brr = [1,2,3,5,5,6]
# arr = [1,2,5,6]
# missingNumbers(arr,brr)

#%%
#dictionary method
# if key in my_dict:
#   my_dict[key] += num
# else:
#   my_dict[key] = num
def missingNumbers(arr, brr):
    dict1 = {}
    for i in brr:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 0
    print(dict1)
    for j in arr:
        if j in dict1:
            dict1[j] -= 1
    result = []
    for k,v in dict1.items():
        if (v>=0):
            result.append(k)
    return sorted(result)
brr = [1,2,3,5,5,6]
arr = [1,2,5,6]
print(missingNumbers(arr,brr))


#%%
