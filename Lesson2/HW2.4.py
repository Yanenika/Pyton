# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

n = int(input("Введите число "))
f1 = int(input("Индекс первого числа  "))
f2 = int(input("Индекс второго числа "))

array = []

for i in range (- n, n + 1):
    array.append(i)
print(array)

p = array[f1 - 1] * array[f2 - 1]

print(p)
