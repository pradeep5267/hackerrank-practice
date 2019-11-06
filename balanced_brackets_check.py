#%%
def balanced_brackets_checker(brackets_stack, brackets_string):
    '''
    the difference between opening and closing brackets <= 3
    '''
    for i in brackets_string:
        if (i == '(' or i == '{' or i == '['):
            brackets_stack.append(i)
        elif (i == ')' or i == '}' or i == ']'):
            if (ord(brackets_stack[-1]) - ord(i) <= 3):
                brackets_stack.pop(-1)
            else:
                print('Not balanced')
                break

    if(len(brackets_stack) == 0):
        print('balanced')


brackets_stack = []
brackets_string = '[()]{}{[()()]()}' #'[(])' 
brackets_string = list(brackets_string)
print(brackets_string)
balanced_brackets_checker(brackets_stack, brackets_string)

#%%
all_brackets = ['(', ')', '{', '}', '[', ']']

for i in all_brackets:
    print(i, ord(i))
