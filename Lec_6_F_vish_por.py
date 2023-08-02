# def f(x):
#     return x*x
# print(f(5))
# print(type(f))
# a = f
# print(type(a))
# print(a(5))

# Переменная а - переменнная, которая хранит в сеье ссылку на функцию f

# def calk_1(a):
#     return a+a

# def calk_2(a):
#     return a*a

# def math(op, x):
#     print(op(x))

# math(calk_2, 5)

# В функцию math мы передаем ссылку на функции calk_1/2

# def calk_1(a, b):
#      return a+b

# calk_1 = lambda a, b : a+b        # дямбда функция - соокращеная запись

# def calk_2(a, b):
#      return a*b

# def math(op, x, y):
#       print(op(x, y))

# # math(calk_1, 5, 45)


# math(lambda a, b : a+b, 5, 45)

# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data :
#     if i % 2 == 0:
#         out.append((i, i ** 2))
# print(out)

# Как вариант

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]

# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res) 
# res = select(lambda x: (x, x*x), res)
# print(res)

# ФУНКЦИЯ map

# 💡 Функция map() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с новыми объектами.

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

# data = '1 2 3 5 8 15 23 38'
# print(data)

# # data = data.split()
# # print(data)

# data = list(map(int, data.split()))
# print(data)


# Функция filter
# 💡 Функция filter() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с теми объектами, для которых
# функция вернула True.

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# Функция zip
# 💡 Функция zip() применяется к набору итерируемых объектов и
# возвращает итератор с кортежами из элементов входных данных

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) 

# ПРОБЕГАЕТ ПО САМОМУ КОРОТКОМУ СПИСКУ

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)


# Функция enumerate
# 💡 Функция enumerate() применяется к итерируемому объекту и
# возвращает новый итератор с кортежами из индекса и элементов входных
# данных.

# Позволяет пронумеровать список данных

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)


