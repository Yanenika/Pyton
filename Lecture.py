# 1. Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.

# a = int(input("a = "))
# b = int(input("b = "))

# if b == a**2 or a == b ** 2:
#     print("Yes")
# else:
#     print("No")    

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

# max = 0
# for i in range(5):
#     n = int(input("n = "))
#     if n > max:
#         max = n
# print(max)   

# Напишите программу, которая будет на вход принимать
# число N и выводить числа от -N до N

# n = int(input(" n = "))

# for i in range(-n, n + 1):
#     print(i)

# 4. Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

# n = float(input(" n = "))
# if n % 10 != 0:
#     new = int(n * 10 % 10)
#     print(new)


# def first_num():
#     n = float(input(" n = "))
#     new_n = int (n * 10 % 10)
#     print(new_n)
# first_num()

# 5. Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

# n = int(input(" n = "))
# if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
#     print("Yes")
# else:
#     print("No")

# 6. Пример проверки ложности утверждения (x ≡ z ) ∨ (x → (y ∧ z))
# print("x y z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not (x == z or x <= y and z):
#                 print(x, y, z)
