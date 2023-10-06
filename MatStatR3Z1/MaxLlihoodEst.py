import openpyxl
import math
import itertools
import scipy.stats

# from itertools import *

book = openpyxl.open("my_r3z1.xlsx", read_only=True)
sheet = book.active

selection = [sheet[row][0].value for row in range(2, sheet.max_row + 1)]
n = len(selection)  # объём выборки
print(n)
"""X = [selection[i][0] for i in range(len(selection))]
Y = [selection[i][1] for i in range(len(selection))]"""
print(*selection)

p = (0.4, 0.5, 0.6)  # вер-ть выпадения орла
s = int(sum(selection))

"""res = list(itertools.product(selection, repeat=n))
print(len(res))"""  # Ужас -- исп. с осторожностью -> был вылет


def likelihood(sel, n, p, tetta):
    prob = 1
    res = list(itertools.product(sel, repeat=n))
    for i in range(n):
        ...
    ...
    return


def L(n, s, tetta):
    return (tetta ** s) * ((1 - tetta) ** (n - s))


def FBern1(n, s, p):
    prob = 1
    probs = []
    for k in range(s):
        for m in range(0, 54 - k):
            for l in range(0, 54 - k - m):
                """for key in p:
                    prob *= p[key]**"""
                # prob *= (p[0]**k)*((1-p[0])**(n-k))\
                # *(p[1]**m)*(p[1]*)\
                # *(p[2]**l)((1-p[0])**(n-k)
                prob *= L(n, s, p[0]) * L(n, s, p[1]) * L(n, s, p[2])
                probs.append(prob)


def calc_probs(p, s, n):
    prob0 = (p[0] ** s) * ((1 - p[0]) ** (n - s))
    prob1 = (p[1] ** s) * ((1 - p[1]) ** (n - s))
    prob2 = (p[2] ** s) * ((1 - p[2]) ** (n - s))
    return (prob0, prob1, prob2)


# prob1 = p[0]**
probs = (calc_probs(p, s, n))
print(probs[0])
probs_dict = {p[0]: probs[0], p[1]: probs[1], p[2]: probs[2]}
maxim = max(probs_dict)


"""for key, value in probs_dict.items():
    if value"""

print(f"Объём выборки: n = {n}")
print(f"Количество успешных исходов (выпадение орла) s = Σxi: {s}")
print(f"Значение функции правдоподобия \nL(Xn | p = 0.4) "
      f"= " + "{0:.80f}".format(probs[0]))
print(f"Значение функции правдоподобия \nL(Xn | p = 0.5) "
      f"= " + "{0:.80f}".format(probs[1]))
print(f"Значение функции правдоподобия \nL(Xn | p = 0.6) "
      f"= " + "{0:.80f}".format(probs[2]))
print(f"Значение оценки, вычисленное на прилагаемых данных: "
      f"p^(Xn)  = argmax(L(Xn | p)) = {maxim}")
# print("Оценка ")
