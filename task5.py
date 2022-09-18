# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))
res = []
resmid = [0, 1]
res2 = []

fnum1 = 0
fnum2 = 1
for i in range(1, k):
    fnum1, fnum2 = fnum2, fnum1 + fnum2
    res.append(fnum2)

fnenum1 = 1
fnenum2 = 0
for i in range(k):
    fnenum1, fnenum2 = fnenum2, fnenum1 - fnenum2
    res2.append(fnenum2)
res2.reverse()

res3 = res2 + resmid + res

print(res3)