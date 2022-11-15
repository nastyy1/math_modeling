import numpy as np
from random import randint

a = np.zeros(4, 3)
b = np.zeros(4, 3)

for i in range(4):
    for j in range(3):
        a[i, j] = randint(0, 100)
        b[i, j] = randint(0, 100)
    

print(a)
print()

print(max(a))

s = 0
for element in a:
  if element > s:
    s = element
print(s)