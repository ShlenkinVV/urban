"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""

def get_pass(first):
    if 3 <= first <= 20:

        result = ""
        for i in range(1, first):
            for j in range(i, first):
                if first % (i + j) == 0 and i != j:
                    result += str(i) + str(j)

        print(result)
    else:
        print('Число введено не верно!')


n = int(input('Введите первое число (от 3 до 20): '))


get_pass(n)
