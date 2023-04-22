# %%
"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
output = 3

"""
# %%
from collections import Counter
from math import floor

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9

dic = Counter(ar)
print(sum(list(map(lambda x: floor(x[1] / 2), dic.items()))))

# %%
