import openpyxl
import math
import scipy.stats

# from itertools import *

book = openpyxl.open("1Alexey_my_r2z1.xlsx", read_only=True)
sheet = book.active

selection = [[sheet[row][0].value, sheet[row][1].value]
             for row in range(2, sheet.max_row + 1)]
X = [selection[i][0] for i in range(len(selection))]
Y = [selection[i][1] for i in range(len(selection))]

Z0 = [0 if X[i] > Y[i] else 1 for i in range(len(X))]
Z1 = [round(X[i] - Y[i], 6) for i in range(len(X))]
select_size = len(Z0)
#print(select_size)
p0 = 0.5
M0 = math.fsum(Z0)
print(f"M0 = {M0}")
M1 = math.fsum(Z1)

alpha = 0.05


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


# print([fact(i) for i in range(11)])


def C(N, k):
    return fact(N) / (fact(k) * fact(N - k))


def Bin(N, k, p):
    return C(N, k) * (p ** k) * ((1 - p) ** (N - k))


def FBin(N, p):
    res = 0
    for k in range(N+1):# N-1 было и N
        # res += C(N, k) * (p ** k) * ((1 - p) ** (N - k))
        res += Bin(N, k, p)
    return res





print("====================================================================================")
print("У исходных выборок X и Y соответствующие i-ые значения сл.в. считаются связанными,\n"
      "а также нет оснований полагать конкретное распределение у X и Y.")
print("Гипотеза H0 — соответствующие значения выборки либо не меняются, либо уменьшаются\n"
      "Гипотеза K (альтернативная) — соответствующие значения выборки увеличивается\n"
      "Исходя из этого критическая область имеет вид: M: M > Cкрит")


def Critical_area(alpha, N, p0):
    mas = []
    prob_mas = []
    all_probs = []
    prob = 0
    # for k in range(N, -1, -1):
    for k in range(N):  # N - 1 было
    # for k in range(N+1, -1, -1): # return max(mas)
        # prob = round(FBin(k, p0), 5)
        prob += Bin(N, k, p0)
        all_probs.append('{0:.15f}'.format(prob))
        # prob = round(FBin(k, p0), 20)
        if prob >= 1 - alpha:
            mas.append(k)
            prob_mas.append(prob)
    for i in range(len(mas)):
        print([mas[i], prob_mas[i]], end=' ')
    print(end='\n')
    for i in range(len(all_probs)):
        print([i, all_probs[i]], end=' ')
    print(end='\n')
    #print(*all_probs)
    return min(mas)


def Hypothesis_choice(M, Crit_area):
    if Crit_area >= M:
        return False
    return True


Crit_area = Critical_area(alpha=0.05, N=select_size, p0=0.5)
# print(1 - alpha)
"""print(f"Bin(21, p0=0,5)={Bin(26, 21, p0)}")
print(f"Bin(20, p0=0,5)={Bin(26, 20, p0)}")
print(f"Bin(19, p0=0,5)={Bin(26, 19, p0)}")
print(f"Bin(18, p0=0,5)={Bin(26, 18, p0)}")
print(f"Bin(17, p0=0,5)={Bin(26, 17, p0)}")
print(f"FBin(26-21=5, p0=0,5)={FBin(26 - 21, p0)}")
print(f"FBin(26-20=6, p0=0,5)={FBin(26 - 20, p0)}")
print(f"FBin(26-19=7, p0=0,5)={FBin(26 - 19, p0)}")
print(f"FBin(26-18=8, p0=0,5)={FBin(26 - 18, p0)}")
print(f"FBin(18, p0=0,5)={FBin(18, p0)}")
print(f"FBin(26-17=9, p0=0,5)={FBin(26 - 17, p0)}")"""
print(f"Критическая константа Скрит равна: {Crit_area}")
print(f"Статистика M критерия: M = Σi(Zi) = {M0}")
print("Так как Cкрит >= T, то выбрана гипотеза Н0" if not (Hypothesis_choice(M0, Crit_area))
      else "Так как Cкрит < T, то выбрана гипотеза K (альтернатива)")
FBin_M0 = 0
for k in range(int(M0)+1):
    FBin_M0 += Bin(select_size, k, p0)
print('{0:.30f}'.format(1 - FBin_M0))

p_value = 1 - FBin(19, p0)
print(f"p-value = " + '{0:.30f}'.format(p_value))
print("====================================================================================")
print(*selection)
print(*X)
print(*Y)
print(*Z0)
print(*Z1)

# print(type(x_value[0]))
