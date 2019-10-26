#%%
def luckBalance(k, contests):
    # k max number of contents to lose 
    ### MVS
    important_contests = 0
    sub_luck = 0
    add_luck = 0
    for i in contests:
        if(i[1] == 1):
            important_contests += 1
    has_to_win = important_contests - k
    print(important_contests, has_to_win)
    contests.sort(key=lambda x: x[0])
    print(contests)
    for i in range(len(contests)):
        if (contests[i][1] == 1 and has_to_win > 0):
                sub_luck += contests[i][0]
                has_to_win -= 1
        else:
            add_luck += contests[i][0]
    final_luck = add_luck - sub_luck
    print(final_luck)




contests1 = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
contests2 = [[13, 1], [10, 1], [9, 1], [8, 1], [13, 1], [12, 1], [18, 1], [13, 1]]
k = 5
luckBalance(k, contests2)

#%%
