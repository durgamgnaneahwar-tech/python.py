# t=(10,20.5,"hello")
# print(t)
# print(type(t))
# print(t[1])

# t=(10,20.5,(10,28.5,"python"),"hello")
# print(t[2][2])
# print(t)
# print(t[-2][-1])

from itertools import product


t=(10,20.5,(10,(11,45.6,45,14,29,"program","language",6.5),28.5,"python"),"hello")
# print(t[2][1][5])
# print(t[2][3])
# print(t[0])
# print(t[-2][-3])

# t=(10)
# print(t)
# print(type(t))

# t=("hello")
# print(t)
# print(type(t))

t=(10,20.5,(10,28.5,"python"),"hello")
# t=t+(100,45,78)
# print(t)
# t=(8,6,12)+t
# print(t)   

# t=[8,54,32]
# print(product(t))

print(t[-1][::-1])































