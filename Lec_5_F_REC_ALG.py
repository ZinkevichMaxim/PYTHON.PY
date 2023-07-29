# Функция - фрагмент программы, используемый многократно
# def (вызов функции) FunctionName(x):

# def sumNumbers(n):
#     summa = 0
#     for i in range(n+1):
#         summa += i
#     return(summa)    #если программа увидела команду return, то работа функции завершается. Поэтом не print


# a = sumNumbers(5)
# print(a)

# КАК ПЕРЕДАТЬ НЕОГРАНИЧЕННОЕ КОЛИЧЕСТВО АРГУМЕНТОВ - СТАВИМ *

# def sum_str(*args):
#     res = ' ' # переменная с типом данных СТРОКА
#     for i in args:
#         res += i
#     return(res)

# print(sum_str('q', 'w', 'e'))
# print(sum_str('q', 'w', 'e', 'y'))

# def sum_int(*args):
#     res = [] # переменная с типом данных СТРОКА  НЕ РАБОТАЕТ
#     for i in args:
#         res.append(i)
#     return(res)
# print(sum_int(1, 2, 3))
# a = sum_int(1, 2, 3, 4)
# print(a)
# print(a[2])

#____________________________________________________________________________________________________________

# МОДУЛИ

# МОДУЛЬ - отдельный файл в котором хранятся функции

# import modul_1
# modul_1.max_1(5, 2)
# print(modul_1.max_1(5, 2))

# # Как вариант

# from modul_1 import max_1
# print(max_1(5, 9))

# Как вариант

# from modul_1 import * - импортирует все функции
# print(max_1(5, 9))

# Как вариант

# import modul_1 as m_1
# print(m_1.max_1(5, 9))

#______________________________________________________________________________________________________________

# РУКУРСИЯ - функция, уоторая вызывает сама себя
# БАЗИС - то место где функции надо остановиться и перестать вызывать саму себя

# ЧИСЛА ФИБОНАЧИ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# # list_1 = []
# # for i in range(10):
# #     list_1.append(fib(i))

# # print(list_1)

# list_1 = []
# for i in range(1, 20):
#     list_1.append(fib(i))

# print(f'И это {list_1}')

#__________________________________________________________________________________________________________

# АЛГОРИТМЫ
# Набор инструкций для выполнения задачи
# БЫСТРАЯ СОРТИРОВКА
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
    
# print(quicksort([10, 5, 2, 3]))

# ● 1-е повторение рекурсии:
# ○ array = [10, 5, 2, 3]
# ○ pivot = 10
# ○ less = [5, 2, 3]
# ○ greater = []
# ○ return quicksort([5, 2, 3]) + [10] + quicksort([])
# ● 2-е повторение рекурсии:
# ○ array = [5, 2, 3]
# ○ pivot = 5
# ○ less = [2, 3]
# ○ greater = []
# ○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что
# здесь помимо вызова рекурсии добавляется список [10]
# ● 3-е повторение рекурсии:
# ○ array = [2, 3]
# ○ return [2, 3] # Сработал базовый случай рекурсии
# На этом работа рекурсии завершилась и итоговый список будет выглядеть таким
# образом: [2, 3] + [5] + [10] = [2, 3, 5, 10]

#____________________________________________________________________________________________________

# Сортировка слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)

#         i = j = k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#                 k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# nums = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(nums)
# print(nums)

# print(sorted(nums))

