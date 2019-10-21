#%%
import math
def gradingStudents(grades):
    # Write your code here
    result = []
    for i in grades:
        tmp = i%10
        if (tmp<=5):
            tmp5 = i + abs(tmp - 5)
        elif(tmp>5):
            tmp5 = i + abs(tmp - 10)
        # print(tmp,tmp5,tmp5-tmp,tmp5-i)
        if (tmp5 - i < 3 and tmp5 >= 40):
            i = tmp5
        result.append(i)

    return result
    # return 0

print(gradingStudents([4,73,67,38,33]))

#%%
print(math.floor(67/10))

#%%
