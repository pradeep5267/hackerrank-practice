#%%
def generate_permutation(chosen_chars, og_string, permutations):
    '''
    the if condition prevents the permutation of duplicates eg: aaaa or
    aaab, etc, since the continue statement if true ignores the lines 
    below and 'continues' on to the next iteration
    So in 1st iteration a is selected as choice and is checked if a is present
    in chosen or not, since chosen is empty a is added to the chosen.
    during the next recursive call i again starts at 0 and hence selects a again
    however the if condition becomes true and loop goes to the next iteration.

    If duplicates are allowed remove the if else conditon
    '''
    if(len(chosen_chars) == len(og_string)):
        tmp = ''.join(chosen_chars)
        permutations.append(tmp)

    for i in range(len(og_string)):
        current_choice = og_string[i]
        print(current_choice, chosen_chars)
        if(current_choice in chosen_chars):
            continue
        else:
        
            # choose
            chosen_chars.append(current_choice)
            
            # explore
            generate_permutation(chosen_chars, og_string, permutations)

            # unchoose
            chosen_chars.pop(-1)
    return permutations

z = list('abcd')
y = generate_permutation([], z, [])
print(y)