import numpy as np
from random import radint

M = 4
N = 5

a = np.zeros((M, N), dtype=int)

for i in range(M):
  for j in range(N):
     a[i, j] = randint(0, 100)

print()
print(a)
print()


a[:, [2, 3]] = a[:, [3, 2]]
print(a)