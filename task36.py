"""
Задача 36:
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
строки и столбца. Аргументы num_rows и num_columns указывают число строк и
столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
называется любая операция, у которой ровно два аргумента, как, например,
у операции умножения.
*Пример:*
**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
"""


def get_number(string):
    try:
        number = int(input(string))
    except ValueError:
        print('Введено не число')
        return get_number(string)
    return number


def print_operation_table(operation, count_rows, count_columns):
    arr = [[operation(i, j) for i in range(1, count_columns + 1)]
           for j in range(1, count_rows + 1)]
    for i in arr:
        print(*[f"{x:>3}" for x in i])


count_rows = get_number('Введите количество строк: ')
count_columns = get_number('Введите количество столбцов: ')
print_operation_table(lambda x, y: x * y, count_rows, count_columns)