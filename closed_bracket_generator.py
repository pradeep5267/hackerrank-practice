#%%
def bracket_generator(brackets, n_open, n_close):
    if(n_open == 0 and n_close == 0):
        print(brackets)
        return
    if (n_open > 0):
        bracket_generator(brackets + '(',n_open - 1, n_close)
    elif (n_open <= n_close):
        bracket_generator(brackets + ')',n_open, n_close - 1)
n = 3
bracket_generator('', n, n)