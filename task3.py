# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# ! ВАЖНО ! В приведенном примере ошибка: 
# минимальное значение дробной части в списке не 0.01, а 0 (у пятерки дробная часть равна нулю),
# поэтому для этого примера правильный ответ 0,2

# fl_list = [1.1, 1.2, 3.1, 5, 10.01]
# res = []
# for i in range(len(fl_list)):
#     res.append(round((fl_list[i]%1), 2))
# print (res)

# res.sort()

# print(res)

# print(res[len(res)-1] - res[0])

# Если требуется найти разность для не целых чисел, то код надо допилить

fl_list = [1.1, 1.2, 3.1, 5, 10.01]
res = []
for i in range(len(fl_list)):
    if fl_list[i]%1 != 0:
        res.append(round((fl_list[i]%1), 2))
print (res)

res.sort()

print(res)

print(res[len(res) - 1] - res[0])
