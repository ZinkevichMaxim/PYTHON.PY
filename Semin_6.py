# ОБЪЯВЛЕНТЕ СЛОВАРЕЙ

# a = [i if i%2==0 else v for i in range(9) for v in "qweqweqwe" ]
# # for i in range(9):
# #     a.append(i)
# print(a)

# b = {key:"q" for key in range(1,5)}
# print(b)
# # for k,v in b.values():
# #     print(k,v)
# for i in range(5,9):
#     b[i] = "qwe"
# print(b)

# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива               
# Ввод: 					Вывод:
# 7					3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1			
	
# a = [3, 1, 3, 4, 2, 4, 12]
# b = [4, 15, 43, 1, 15, 1]
# c = []
# for i in range(len(a)):
#     if a[i] not in b:
#         c.append(a[i])
# print(c)
#________________________________________________________________________________________________________________-
# ВАРИАНТ 2
# a = [3, 1, 3, 4, 2, 4, 12]
# b = [4, 15, 43, 1, 15, 1]
# c = []
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == b[j]:
#             break
#     else:
#         c.append(a[i])
# print(c)



# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве выведет количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве  
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 

# Ввод: 			Ввод:
# 5				5
# 1 2 3 4 5			1 5 1 5 1

# Вывод:			Вывод:
# 0				2
				
# a = [1, 2, 3, 4, 5]
# a = [1, 5, 1, 5, 1]
# c = []
# i = 1
# for i in range(len(a) - 1):
#     if a[i-1]<a[i]>a[i+1]:
#         c.append(a[i])
# print(len(c))

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод:			Вывод:
# a = [1, 2, 3, 2, 3]	#		2

# a = [1, 2, 3, 2, 3, 1, 2]
# count = 0
# for i in range(len(a)):
#     for y in range(i + 1, len(a)):
#         if a[i] == a[y]:
#             count += 1

# print(count)


# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:			Вывод:
# 300			220 284
# k = int(input('Введите число: '))
# new_cikl = []
# for i in range(1, k):
#     summ = 0
#     for j in range(1, i//2 + 1):
#         if i % j == 0:
#             summ += j
#     new_cikl.append([i, summ])

# for i in range(len(new_cikl)):
#     for j in range(i + 1, len(new_cikl)):
#         if new_cikl[i][0] == new_cikl[j][1] and new_cikl[j][0] == new_cikl[i][1]:
#             print (new_cikl[i])
    
        
		# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# def stepen(a,b, res = 1, count = 1):
#     print(f"a = {a}, b = {b}, res = {res},count = {count}")
#     if b == 0:
#         return res
#     a = stepen(a,b-1,res*a,count+1)
#     print(a,count)
#     return a
# a = int(input())
# b = int(input())
# print(stepen(a,b))


# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# def sum(a,b):
#     if b == 0:
#         return a
#     return sum(a+1,b-1)
# a = int(input())
# b = int(input())
# print(sum(a,b))