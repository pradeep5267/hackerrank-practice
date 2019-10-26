#%%
def gridMaker(grid):
    '''working solution'''
    sgrid = [sorted(row) for row in grid]
    for col in zip(*sgrid):
        if any(ord(col[i+1]) < ord(v) for i,v in enumerate(col[:-1])):
            return 'NO'
    return 'YES' 
def grid_reorder(grid):
    grid = [list(i) for i in grid ]
    print(grid)
    for i in range(len(grid)):
        grid[i].sort()
    for i in range(len(grid)-1):
        print(grid[i][0], grid[i+1][0])
        tmp1 = str(grid[i][0])
        tmp2 = str(grid[i+1][0])
        if (tmp1 < tmp2) is False:
            return 'NO'
    return 'YES'


grid = ['eabcd',
'fghij',
'olkmn',
'trpqs',
'xywuv']
print(grid_reorder(grid))


#%%
