#%%
def Candies3(arr):
    '''
    attempt 3: PASS
    looked at the solution, though the plan seems the same, the
    implementation makes 2 seperate passes, one for forward and 
    one for backward checks
    and also uses a list to store values instead of variables
    '''
    '''
    First, make sure I have right number of candy 
    when compared to my left kid.

    Then, make sure I have the right number of candy 
    when compared to my right kid.
    '''
    '''
    REMEMBER TO ALWAYS LOOK AT PAST INSTANCES AND NOT FUTURE
    IE (I-1) AND NOT (I+1)
    '''
    n = len(arr)
    candie_list = [1]*n
    # candie_list.append(0)

    # look back
    for i in range(1, n):
        # if (candie_list[i] == 0):
        #     candie_list[i] = 1
        if (arr[i] > arr[i-1]):
            # standing at i, check whether the i-1 is smaller;
            # if true give i one more candie than i-1
            candie_list[i] = candie_list[i-1] + 1
    
    # look forward
    for i in range(n-2, -1, -1):
        print(i, i+1, candie_list[i], candie_list[i+1])
        if (arr[i] > arr[i + 1]):
            # here compare the candies and give the highest candies between
            # the 2 to i;
            # another way is to check if the candies of i is 
            # less than OR EQUAL to i+1, this <= is necessary since 
            # both i and i+1 would be having 1 candie by default and 
            # during backward pass i might have been less than i-1
            # but during forward pass i will be greater than i+1
            ### basically an edge case
            candie_list[i] = max(candie_list[i] ,candie_list[i+1] + 1)
            # candie_list[i] = candie_list[i + 1] + 1
    print(candie_list, sum(candie_list))

arr1 = [1, 2, 2] #4
arr2 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1] #19
arr3 = [2, 4, 3, 5, 2, 6, 4, 5] #12
result = Candies3(arr3)
%%
def Candies1(arr):
    '''
    MVC
    attempt 1: FAILED
    was to fix a pointer at index 1 and check forward and backward,
    didnt work because
    '''
    n = len(arr)
    i = 0
    j = 1
    # current_candie = 1
    candie_sum = 1
    tmp_candie_holder = []
    min_candie = 1
    previous_max_candie = 1
    # arr.insert(0, -1)

    for i in range(0, len(arr) - 1):
        if (i > 0):
            if(arr[i-1] > arr[i]):
                previous_max_candie += 1
            else:
                previous_max_candie = 1
        if(arr[i] > arr[i+1] or arr[i] < arr[i+1]):
            candie_sum += previous_max_candie + previous_max_candie + 1
            # tmp_candie_holder.append(previous_max_candie)
            tmp_candie_holder.append(previous_max_candie + 1)
        elif (arr[i] == arr[i+1]):
            candie_sum += previous_max_candie + previous_max_candie
            # tmp_candie_holder.append(previous_max_candie)
            tmp_candie_holder.append(previous_max_candie)
    print(candie_sum)
    print(tmp_candie_holder)


arr1 = [1, 2, 2] #4
arr2 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1] #19
arr3 = [2, 4, 3, 5, 2, 6, 4, 5] #12
result = Candies1(arr3)
#%%
def Candies2(arr):
    '''
    attempt 2: FAILED
    because it is the same implementation of attempt
    1 with hardcoded edge cases
    '''
    current_max = 1
    candie_sum = len(arr)
    # i = 0 # i corresponds to index and not position
    i = 0
    while i <= len(arr) - 1:
        # edge case 
        if(i == 0):
            if (arr[i] > arr[i+1] or arr[i] < arr[i+1]):
                current_max += 1
                candie_sum += current_max

        if (i == 1):
            i += 1 
            continue
        if(arr[i] > arr[i-1]):
            current_max += 1
            candie_sum += current_max
        else:
            current_max = 1
        i += 1
    print(candie_sum)

arr1 = [1, 2, 2] #4
arr2 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1] #19
arr3 = [2, 4, 3, 5, 2, 6, 4, 5] #12
arr4 = [2,4,3,5,2,6,4,5]

result = Candies(arr3)
