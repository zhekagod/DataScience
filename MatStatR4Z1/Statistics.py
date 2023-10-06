import Data as dt
import math as m

select_size = len(dt.selection)  # объём выборкиH
# min_select = min(dt.selection)  # минимум
# max_select = max(dt.selection)  # максимум
# scale = max_select - min_select  # размах
counting = int(select_size / 10)


# width = scale / counting  # толщина столбцов


# (интервал) дельта
# print(f"widht = {width}")


def expected_value(sel, sel_size):  # мат.ожидание
    return sum(sel) / sel_size


# print("============================================================")

"""print(f"Объём выборки: {select_size}")
print(f"Минимум: {min_select}")
print(f"Максимум: {max_select}")
print(f"Размах: {scale}")
print(f"Мат ожидание: "
      f"{expected_value(dt.selection, select_size)}")"""


def sq(x):
    return x ** 2


def variance(sel, sel_size):  # смещённая дисперсия
    result = 0
    exp = expected_value(sel, sel_size)
    for i in range(len(sel)):
        result += sq(sel[i] - exp)
    return result / sel_size


"""print(f"Смещённая выборочная дисперсия: "
      f"{variance(dt.selection, select_size)}")"""


def unbiased_variance(sel, sel_size):  # несмещённая дисперсия
    return (variance(sel, sel_size) * sel_size) / (sel_size - 1)


"""print(f"Несмещённая выборочная дисперсия: "
      f"{unbiased_variance(dt.selection, select_size)}")"""


def deviation(sel, sel_size):
    return m.sqrt(variance(sel, sel_size))


# print(f"Стандартное отклонение: {deviation(dt.selection, select_size)}")


def correlation(sel1, sel1_size, sel2, sel2_size):
    return ...


def selective_correlation(sel1, sel2, n):
    r = 0
    exp1 = expected_value(sel1, n)
    exp2 = expected_value(sel2, n)
    dev1 = deviation(sel1, n)
    dev2 = deviation(sel2, n)
    for i in range(n):
        r += ((sel1[i] - exp1)*(sel2[i] - exp2))
    return r/(n*dev1*dev2)


def assymerty(sel, sel_size):
    result = 0
    exp = expected_value(sel, sel_size)
    for i in range(len(sel)):
        result += (sel[i] - exp) ** 3
    return result / (sel_size * (deviation(sel, sel_size) ** 3))


# print(f"Ассиметрия: {assymerty(dt.selection, select_size)}")


def median(sel, sel_size):
    if sel_size % 2 == 1:
        return sel[int(sel_size / 2)]
    return (sel[int(sel_size / 2)] + sel[int(sel_size / 2) - 1]) / 2


# print("Медиана: ", median(dt.selection, select_size))


def shirota(sel, sel_size, q):
    if (sel_size - 1) * q == int((sel_size - 1) * q):
        return sel[(sel_size - 1) * q + 1]
    elif (sel_size - 1) * q > int((sel_size - 1) * q):
        return (sel[int((sel_size - 1) * q) + 1] + sel[int((sel_size - 1) * q) + 2]) / 2


"""print("Интерквартильная широта: ", shirota(dt.selection, select_size, (3 / 4)) -
      shirota(dt.selection, select_size, (1 / 4)))"""

# print("============================================================")
