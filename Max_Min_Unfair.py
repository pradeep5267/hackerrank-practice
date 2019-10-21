#%%
import sys
def MaxMin(k, arr):
    '''
    1)sort 
    2)set min_value as the biggest possible int
    3)set j = k-1 since while looping setting the values
    as j-1 leads to last element being not accessed;
    since the condition is set at j <= n, therefore when j = n
    the value it would be accessing would be j = n-1 (since j-1)
    4)since arr is sorted, ith element would be smallest and jth element 
    would be biggest in the subarray
    5)calculate unfairness by jth - ith
    6)find the smallest unfairness for the different sub arrays
    

    '''
    arr.sort()
    n = len(arr)
    n -= 1
    min_value = sys.maxsize
    i, j, tmp = 0, k-1, 0
    while j <= n :        
        tmp = (arr[j]-arr[i])
        if (tmp < min_value):
            min_value = tmp
            min_index = i
            i += 1
            j += 1
        else:
            i += 1
            j += 1
    print(min_value,min_index-1)

# def MaxMin(k, arr):
#     arr.sort()
#     n = len(arr)
#     n -= 1
#     min_value = sys.maxsize
#     i, j, tmp = 0, k, 0
#     while i <= n and j <= n :        
#         tmp = (max(arr[i:j]) - min(arr[i:j]))
#         if (tmp < min_value):
#             min_value = tmp
#             min_index = i
#             i += 1
#             j += 1
#         else:
#             i += 1
#             j += 1
#         # if (i < min_value):
#         #     min_value = i
        
#     print(min_value)



k = 3
# c = [1, 3, 5, 7, 9] # len of c = n
# c = [10,100,300,200,1000,20,30]
c = [100,200,300,350,400,401,402]
MaxMin(k,c)

#%%
