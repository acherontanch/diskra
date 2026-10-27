import random
from sage.all import *
print("Таблица")
border = "~"*30
print(border)
n = 3
Matrix = matrix(ZZ, n, n, lambda i, j: ZZ.random_element(0,n))
print(Matrix)
print(border)
S = all(Matrix[i, j] == Matrix[j, i]
        for i in range(1, n)
        for j in range(i))
if S:
    print("коммутативна")
else:
    print("Не коммутативна")
    