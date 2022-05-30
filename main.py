# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
print(f'Исходный список: {my_list}')
for i in range(0, len(my_list)):
    if (isinstance(my_list[i], float)):
        # взял именно "isinstance()",
        # потому что проверка остатка деления на 1
        # не отбросит целое число (5/1=5.0).
        my_list[i] = float('0.' + (str(my_list[i]).split('.'))[1])
print(f'Изменённый список: {my_list}')
max_el = my_list[0]
min_el = my_list[0]
for i in range(0, len(my_list)):
    if (isinstance(my_list[i], float) and max_el < my_list[i]):
        max_el = my_list[i]
for i in range(0, len(my_list)):
    if (isinstance(my_list[i], float) and min_el > my_list[i]):
        min_el = my_list[i]
print(f'Разница между максимальным и минимальным значением дробной части элементов списка={max_el - min_el}')
