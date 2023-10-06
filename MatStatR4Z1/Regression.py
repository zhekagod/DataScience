import numpy as np
import matplotlib.pyplot as plt
import Data as dt
import Statistics as stat
import random

plt.figure(figsize=(8, 6))
plt.subplot().scatter(dt.x_value, dt.y_value, alpha=0.4)
plt.ylabel("Случайная величина Y")
plt.xlabel("Случайная величина X", color='red')
plt.title("Ось абсцисс — X, ось ординат — Y")

# coef = 0.19459214
Data_X = [[i, dt.x_value[i]] for i in range(len(dt.x_value))]
Data_Y = [[i, dt.y_value[i]] for i in range(len(dt.y_value))]

X = [dt.x_value[i] for i in range(len(dt.x_value))]
Y = [dt.y_value[i] for i in range(len(dt.y_value))]


size_X = len(X)
size_Y = len(Y)
n = size_X

exp_X = stat.expected_value(X, n)
dev_X = stat.deviation(X, n)
var_X = stat.variance(X, n)
exp_Y = stat.expected_value(Y, n)
var_Y = stat.variance(Y, n)
dev_Y = stat.deviation(Y, n)
r = stat.selective_correlation(X, Y, n)

print("Выборка X: ")
print(f"Матетическое ожидание выборки X = {exp_X}")
print(f"Дисперсия выборки X = {var_X}")
print(f"Стандартное отклонение выборки X = {dev_X}")
print()
print("Выборка Y: ")
print(f"Матетическое ожидание выборки Y = {exp_Y}")
print(f"Дисперсия выборки Y = {var_Y}")
print(f"Стандартное отклонение выборки Y = {dev_Y}")
print()
print(f"Выборочная корреляция Corr(X;Y) = {r}")
print()

k = r * dev_X / dev_Y
b = exp_X - k * exp_Y
y = np.linspace(min(Y), max(Y), len(Y))
x = k * y + b

print(f"Уравнение регрессии: x = {k}*y + {b}")
print(f"Прогноз регрессии при Y = 82: x(82) = {k * 82 + b}")
# X = 0.4034455482748431*x + 88.33657920281877
# y = 0.19459214*x + 59.88

plt.subplot().plot(x, y, color='green', linewidth=3)
plt.scatter(k * 82 + b, 82, color='black', marker="o")

plt.show()
