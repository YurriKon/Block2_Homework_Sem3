# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_a = [2, 3, 4, 5, 6]
res = []
i = 0
k = len(list_a) - 1
while i < k:
    res.append(list_a[i] * list_a[k])
    i += 1
    k -= 1
if i == k:
    res.append(list_a[i] * list_a[i])
print(res)



