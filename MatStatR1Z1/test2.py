import openpyxl
import numpy
import matplotlib.pyplot as plt
import seaborn

book = openpyxl.open("my_r1z1.xlsx", read_only=True)
sheet = book.active

data = list()
for i in range(2, sheet.max_row + 1):
    data.append(sheet[i][0].value)

data.sort()

X0 = data[0]
print("Минимум: ", X0)

Xn = data[len(data) - 1]
print("Максимум: ", Xn)

print("Размах: ", Xn - X0)

n = len(data)
print("Объём выборки: ", n)

summa = 0
for i in data:
    summa += i
M = summa / n
print("Среднее: ", M)

summa = 0
for i in data:
    summa += i * i
S_pow_2_1 = (summa / n) - M * M
print("Смещённая выборочная дисперсия: ", S_pow_2_1)

S_pow_2_2 = (n / (n - 1)) * S_pow_2_1
print("Несмещённая выборочная дисперсия: ", S_pow_2_2)

S = S_pow_2_1 ** 0.5
print("Стандартное отклонение: ", S)

summa = 0
for i in data:
        summa += (i - M) ** 3
g1 = summa / n / (S ** 3)
print("Асимметрия: ", g1)

if n % 2 == 1:
    m = data[int(n / 2)]
else:
    m = (data[int(n / 2)] + data[int(n / 2) - 1]) / 2
print("Медиана: ", m)


def Q(data, q):
    if (n - 1) * q == int((n - 1) * q):
        return data[(n - 1) * q + 1]
    elif (n - 1) * q > int((n - 1) * q):
        return (data[int((n - 1) * q) + 1] + data[int((n - 1) * q) + 2]) / 2


print("Интерквартильная широта: ", Q(data, (3 / 4)) - Q(data, (1 / 4)))


fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()

x = numpy.linspace(min(data), max(data), 13)
bar_y = [0 for i in range(len(x) - 1)]
ind = 0
for i in range(1, len(x)):
    for j in range(ind, len(data)):
        if x[i - 1] <= data[j] < x[i]:
            bar_y[i - 1] += 1
            ind += 1
bar_y = [i / (x[1] - x[0]) / n for i in bar_y]


bar_x = list()
for i in range(len(x) - 1):
    if i < (len(x) - 1) / 2:
        bar_x.append(x[i] + 0.75)
    else:
        bar_x.append(x[i] + 0.40)

ax.bar(bar_x, bar_y, width=1.5)
# seaborn.kdeplot(data, color="red")
ax.grid()

plt.show()

def plot_empirical_cdf(sample):
    count = 1
    for i in range(len(sample) - 1):
        if not(sample[i] == sample[i + 1]):
            plt.plot([sample[i], sample[i + 1]], [count / len(sample), count / len(sample)])
        count += 1
    plt.plot([sample[len(sample) - 1], sample[len(sample) - 1] + 1], [1, 1])
    plt.show()


plot_empirical_cdf(data)






































# book = openpyxl.open("Ainur1_r1z1.xlsx", read_only=True)