#%%
x =[1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
s = 'zaba'
m = 0
for i in s:
    c = ord(i)-97
    print(c,x[c],'\n')
    if(x[c] > m):
        m = x[c]
print(m, m*len(s))
# %%
