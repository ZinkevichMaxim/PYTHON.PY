# # Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# # Количество повторов добавляется к символам с помощью постфикса формата _n.

# .split(разделитель) - разделяет СТРОКУ на массив

# s = input()
# print(s.split())
# l = ['в', 'в', 'в', 'а', 'а', 'а']
# print(' '.join(l))     # Обратная функция Преобразует массив в строку

# ФУНКЦИЯ .get()

# d = {'a': 123, 's':456}
# # print(d['a'])      == print(d.get('a')) Функция  .get() при несуществующем ключе выдает не ошибку а None/или другое указанное значение:
# print(d.get('q')) # None
# print(d.get('q', 0))   # 0

# s = input('Введите строку \n').split( )
# dict_res  = {}
# for i in s:
#     if i not in dict_res:     #если I нет в словаре, то:
#         print(i, end=' ')    #разделитель пробел
#     else:
#         print(f'{i}_{dict_res[i]}', end= ' ')
#     dict_res[i] = dict_res.get(i, 0) + 1


#---------------------------------------------------------------------------
#Пользователь вводит текст(строка). Словом считается последовательность непробельных символов 
# идущих подряд, слова разделены одним пробелом. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 15

# stroca = input('Введите строку \n').split()
# set_s = set(stroca)
# print(len(set_s))

#--------------------------------------------------------------------------------------------

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем
# (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до 
# конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи
# обратились к Вам, студентам.

# Примечание: Программные коды на следующих слайдах
"""
1 
2
5
1
7
3
0
-> 7
"""
# 7 5 1 5 2

n = int(input('In '))
max_n = n
while n != 0:
    n = int(input('In '))
    if n > max_n:
        max_n = n
print(max_n)

