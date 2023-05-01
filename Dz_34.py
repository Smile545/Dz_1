import random

list = []
a = int(input("Введите длину массива "))

for i in range(a):
    list.append(random.randint(0,1000))
print(list)
min = int(input("Введите минимальное значение "))
max = int(input("Введите максимальное значение "))

for i in range(len(list)):
    if min <= list[i] <= max:
        print(i)