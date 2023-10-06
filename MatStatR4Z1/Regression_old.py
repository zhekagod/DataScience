import numpy as np
import matplotlib.pyplot as plt
import Data as dt
import Statistics as stat
import pandas as pd
from sklearn.linear_model import LinearRegression

"""fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()"""
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1).scatter(dt.x_value, dt.y_value, alpha=0.4)
plt.ylabel("Случайная величина Y")
plt.xlabel("Случайная величина X", color='red')
plt.title("Ось абсцисс — X, ось ординат — Y")
rnd_data = pd.read_excel("my_r4z2.xlsx")

"""X = [dt.x_value]

Y = [dt.y_value]"""

X = pd.DataFrame(rnd_data.X)
Y = pd.DataFrame(rnd_data.Y)
#print(X)

"""model = LinearRegression()
model.fit(Y, X)
#print(model.fit(X, Y))
#print(f"coef = {model.coef_}")
#print(f"b_coef = {model.rank_}")
plt.plot(model.predict(Y), Y,
         color='red', linewidth=5)"""

# coef = 0.19459214
Data_X = [[i, dt.x_value[i]] for i in range(len(dt.x_value))]
Data_Y = [[i, dt.y_value[i]] for i in range(len(dt.y_value))]
X = [dt.x_value[i] for i in range(len(dt.x_value))]
Y =[dt.y_value[i] for i in range(len(dt.y_value))]
size_X = len(X);
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

k = r*dev_X/dev_Y
b = exp_X - k*exp_Y
"""x = np.linspace(min(X), max(X), len(X))
print(f"y = {k}*x + {b}")
y = k*x + b"""
y = np.linspace(min(Y), max(Y), len(Y))
x = k*y + b

print(f"Уравнение регрессии: x = {k}*y + {b}")
print(f"Прогноз регрессии при Y = 82: x(82) = {k*82 + b}")
# X = 0.4034455482748431*x + 88.33657920281877
# y = 0.19459214*x + 59.88

plt.subplot(1, 2, 1).plot(x, y, color='green', linewidth=3)
plt.scatter(k*82 + b, 82, color='black', marker="o")


plt.subplot(1, 2, 2)
"""X = pd.DataFrame(rnd_data.X)
Y = pd.DataFrame(rnd_data.Y)
plt.plot(Y, model.predict(Y),
         color='red', linewidth=5)"""

plt.scatter(dt.y_value, dt.x_value, alpha=0.4)
plt.ylabel("Случайная величина X", color='red')
plt.xlabel("Случайная величина Y")
plt.title("Ось абсцисс — Y, ось ординат — X")
plt.plot(y, x, color='cyan', linewidth=3)
plt.scatter(82, k*82 + b, color='black', marker="o")








plt.show()


"""y = 0.19459214*x+1
ax.plot(x, y, color='yellow')
print(X)


ax.grid()
plt.show()"""
