# 1. Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов.
# def n_func():
#     for i in range(int(input("введите число n "))):
#         print((-3) ** i, end = ' ')
# n_func()

# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
# где k принимает значения от 1 до n включительно.

# num_list = []
# n = int(input(" n = "))
# for k in range (1, n +1):
#     num_list.append (3 * k + 1)
# print (num_list)

# 3. Напишите программу, в которой пользователь будет задавать две строки,
# программа - определять количество вхождений одной строки в другой.
n = input("Введите пердложение")
m = input("повторяющие слоги или буквы")
print(n.count(m))

