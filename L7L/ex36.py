def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            element = operation(row, column)
            print(element, end="\t")
        print()

# Пример использования

# Функция, вычисляющая элементы таблицы как сумму номеров строки и столбца
def sum_operation(row, column):
    return row + column

# Печать таблицы с использованием функции sum_operation
print_operation_table(sum_operation, num_rows=4, num_columns=5)