import numpy as np
import matplotlib.pyplot as plt
import Data as dt
import Statistics as stat
import random

"""plt.figure(figsize=(8, 6))
plt.subplot().scatter(dt.x_value, dt.y_value, alpha=0.4)
plt.ylabel("Случайная величина Y")
plt.xlabel("Случайная величина X", color='red')
plt.title("Ось абсцисс — X, ось ординат — Y")"""

# coef = 0.19459214
Data_X = [[i, dt.x_value[i]] for i in range(len(dt.x_value))]
Data_Y = [[i, dt.y_value[i]] for i in range(len(dt.y_value))]

"""X = [dt.x_value[i] for i in range(len(dt.x_value))]
Y = [dt.y_value[i] for i in range(len(dt.y_value))]"""

X1 = [random.uniform(-6, 0) for i in range(100)]
Y1 = [random.uniform(-4, 0) for i in range(100)]

X2 = [random.uniform(2, 6) for i in range(100)]
Y2 = [random.uniform(0, 4) for i in range(100)]

for i in X2:
    X1.append(i)
for j in Y2:
    Y1.append(j)

plt.figure(figsize=(8, 6))
plt.subplot().scatter(X1, Y1, alpha=0.5)
plt.ylabel("Случайная величина Y")
plt.xlabel("Случайная величина X", color='red')
plt.title("Ось абсцисс — X, ось ординат — Y")



size_X1 = len(X1)
size_Y1 = len(Y1)
n1 = size_X1

exp_X1 = stat.expected_value(X1, n1)
dev_X1 = stat.deviation(X1, n1)
var_X1 = stat.variance(X1, n1)
exp_Y1 = stat.expected_value(Y1, n1)
var_Y1 = stat.variance(Y1, n1)
dev_Y1 = stat.deviation(Y1, n1)
r1 = stat.selective_correlation(X1, Y1, n1)

print("Выборка X: ")
print(f"Матетическое ожидание выборки X = {exp_X1}")
print(f"Дисперсия выборки X = {var_X1}")
print(f"Стандартное отклонение выборки X = {dev_X1}")
print()
print("Выборка Y: ")
print(f"Матетическое ожидание выборки Y = {exp_Y1}")
print(f"Дисперсия выборки Y = {var_Y1}")
print(f"Стандартное отклонение выборки Y = {dev_Y1}")
print()
print(f"Выборочная корреляция Corr(X;Y) = {r1}")
print()

k1 = r1 * dev_X1 / dev_Y1
b1 = exp_X1 - k1 * exp_Y1
y1 = np.linspace(min(Y1), max(Y1), len(Y1))
x1 = k1 * y1 + b1

plt.subplot().plot(x1, y1, color='green', linewidth=3)

k1 = r1 * dev_Y1 / dev_X1
b1 = exp_Y1 - k1 * exp_X1
x1 = np.linspace(min(X1), max(X1), len(X1))
y1 = k1 * x1 + b1

plt.subplot().plot(x1, y1, color='red', linewidth=3)

print(f"Уравнение регрессии: x = {k1}*y + {b1}")
print(f"Прогноз регрессии при Y = 82: x(82) = {k1 * 82 + b1}")
# X = 0.4034455482748431*x + 88.33657920281877
# y = 0.19459214*x + 59.88


#plt.scatter(k1 * 82 + b1, 82, color='black', marker="o")

plt.show()
