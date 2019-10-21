#%%
from collections import defaultdict
d = defaultdict()
l1 = ["eat","sleep","repeat"] 
s1 = "geek"
  
# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
  
# print ("Return type:",type(obj1))
# print (enumerate(l1))

# print(obj1.__doc__)
z = {count:value for count,value in enumerate(l1)}
print(z)
#%%
def list_parser(lst):
    for x in lst:
        print(x)
z = [1,2,3]
y = 'str'
list_parser(z)
list_parser(y)

#%%
%%timeit
def dyna_fib(n, lookup):
    if n <= 2: 
        lookup[n] = 1 
    
    if lookup[n] is None: 
        lookup[n] = dyna_fib(n-1, lookup) + dyna_fib(n-2, lookup) 
    
    return lookup[n]

n = 9
lookup = [None]*(n+1)
x = dyna_fib(n,lookup)
print(x)
#%%
count = 0
def fib(n): 
    if n >= 2:
       return sum += fib(n
    else: 
        return fib(n-1) 




print(fib(9)) 


#%%
