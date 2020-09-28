#%%
s1 = 'a bb ccccc ddd'
l2 = []
l2 = ''.join(s1.split())
l2 = list(l2)
print(l2)
d1 = {}
for i in l2:
    if not i in d1:
        d1[i] = 1
    else:
        d1[i] += 1
print(d1)

# %%

print(d1.get('a'))


# %%
