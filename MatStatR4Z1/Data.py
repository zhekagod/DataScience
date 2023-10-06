import openpyxl
import pandas as pd

book = openpyxl.open("my_r4z2.xlsx", read_only=True)

sheet = book.active

# print(sheet["A3"].value)
# Нумерация рядов с 1, а колонок с 0
selection = [[sheet[row][0].value, sheet[row][1].value]
             for row in range(2, sheet.max_row + 1)]
# print(*selection)
x_value = [selection[i][0] for i in range(len(selection))]
y_value = [selection[i][1] for i in range(len(selection))]
# print(f"len = {len(selection)}")
# print(*x_value)
# print(*y_value)
