G1 = [[0, 1, 1, 0, 0, 1, 1],
      [1, 0, 1, 1, 0, 0, 1],
      [1, 1, 0, 1, 1, 0, 0],
      [0, 1, 1, 0, 1, 1, 0],
      [0, 0, 1, 1, 0, 1, 1],
      [1, 0, 0, 1, 1, 0, 1],
      [1, 1, 0, 0, 1, 1, 0]]
G1 = [[0, 1, 1, 1, 1, 0, 0],
      [1, 0, 1, 1, 0, 1, 0],
      [1, 1, 0, 0, 0, 1, 1],
      [1, 1, 0, 0, 1, 0, 1],
      [1, 0, 0, 1, 0, 1, 1],
      [0, 1, 1, 0, 1, 0, 1],
      [0, 0, 1, 1, 1, 1, 0]]
G2 = [[0, 1, 0, 1, 1, 0, 1],
      [1, 0, 1, 0, 1, 1, 0],
      [0, 1, 0, 1, 0, 1, 1],
      [1, 0, 1, 0, 1, 0, 1],
      [1, 1, 0, 1, 0, 1, 1],
      [0, 1, 1, 0, 1, 0, 1],
      [1, 0, 1, 1, 0, 1, 0]]

import numpy as np

I = [0, 1, 2, 3, 4, 5, 6]
P = [0, 5, 3, 1, 6, 4, 2]
newG2 = [[G2[P[i]][P[j]] for j in I] for i in I]

# print(*G1)
# print(*G2)
print("G1: ")
for i in range(7):
    for j in range(7):
        print(G1[i][j], end=" ")
    print(end='\n')
print("G2: ")
for i in range(7):
    for j in range(7):
        print(G2[i][j], end=" ")
    print(end='\n')
"""print("G2_new0: ")
G2_1 = [G2[0], G2[5], G2[3], G2[1], G2[6], G2[4], G2[2]]
for i in range(7):
    for j in range(7):
        print(G2_1[i][j], end=" ")
    print(end='\n')
print("G2_new1: ")
for i in range(7):
    for j in range(7):
        print(newG2[i][j], end=" ")
    print(end='\n')"""
idx = [0, 5, 3, 1, 6, 4, 2]
x = np.array(G2)
res = x[idx]
res = res[:, idx]
# print(*res)
print("G2_new2: ")
for i in range(7):
    for j in range(7):
        print(res[i][j], end=" ")
    print(end='\n')
print(newG2 == res)
"""a = int(input("Введите a: "))
b = int(input("Введите b: "))
while((a != 9 or b != 9) or (G2 != G1)):
  G2[a-1], G2[b-1] = G2[b-1], G2[a-1]
  #tmpG2a = G2[a]
  #tmpG2b = G2[b]
  #G2[a] = tmpG2b
  #G2[b] = tmpG2a
  print("G2: ")
  for i in range(7):
    for j in range(7):
      print(G2[i][j], end=" ")
    print(end='\n')
  if (G2 == G1):
    print("G2 ~ G1")
    break
  a = int(input("Введите a: "))
  b = int(input("Введите b: ")) """
