#%%
import sys
def JimOrder(tuple_arr):
    i = 1
    order_dict = {}
    order_list = []
    # (order, prep_time)
    # order_dict = {order:(order+prep) for prep, order in tuple_arr}
    for prep, order in tuple_arr:
        order_dict[i] = order+prep
        i += 1
    for w in sorted(order_dict, key=order_dict.get):
        order_list.append(w)
    return(order_list)

x = [(8, 1),
(4, 2),
(5, 6),
(3, 1),
(4, 3)]

JimOrder(x)

#%%
