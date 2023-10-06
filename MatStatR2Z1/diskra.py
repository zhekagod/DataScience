import numpy as np
#    0, 1, 2
x = [
    [0, 1, 0],  # 0
    [1, 0, 1],  # 1
    [0, 1, 0]   # 2
]

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=' ')
    print(end='\n')

idx = [0, 2, 1] # новый порядок

x = np.array([  # приводим 2-м список в массив numpy
    [0, 1, 0],  # 0
    [1, 0, 1],  # 1
    [0, 1, 0]   # 2
])

res=x[idx]
res=res[:,idx]
print()
for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j],end=' ')
    print(end='\n')
I = [0, 1, 2]  # начальное положение строк и столбцов
P = [0, 2, 1]  # конечное положение строк и столбцов
res = [[x[P[i]][P[j]] for j in I] for i in I]
print()
for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j],end=' ')
    print(end='\n')