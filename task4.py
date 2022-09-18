# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

decnum = int(input('Введите число: '))

binum = ""

while decnum > 0:
    binum = str(decnum % 2) + binum
    decnum = decnum // 2
print(binum)