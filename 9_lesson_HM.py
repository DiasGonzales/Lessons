##############################################################################
# 1)Пользователь вводит число. Проверьте, 
# является ли оно кратным 5, и выведите соответствующее сообщение.

# num = int(input())

# if not num % 5:
#     print('введнное число кратно 5') 
# else:
#     print('введенное число не кратно 5')
    
###############################################################################    
    
    
#  2)Пользователь вводит текущий час (целое число от 0 до 23). 
#  Выведите сообщение, указывающее на время суток: "Доброе утро", 
#  "Добрый день", "Добрый вечер" или "Спокойной ночи". 

# clock = int(input())
# if clock < 11:
#     print('Доброе утро')
# elif clock > 11 and clock < 17:
#         print('Добрый день')
# elif clock > 17 and clock < 21:
#         print('Добрый вечер')
# else:
#     print('Спокойной ночи')
        
###############################################################################      
        
# 3)Определение максимума. Пользователь вводит три числа. 
# Найдите и выведите наибольшее из них. 

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print(max(num1, num2, num3))

###############################################################################

#  4)Пользователь вводит положительное целое число n. 
#  Найдите сумму всех чисел от 1 до n и выведите результат.


# num = int(input('Введите ваше число: '))
# a = []

# for i in range(1, num + 1):
#     a.append(i)

# sum_of_num = sum(a)
# print(sum_of_num)

###############################################################################

# 5)Создайте файл "data.txt" и запишите в него список чисел 
#  (каждое число на отдельной строке). Напишите программу, 
#  которая открывает файл "data.txt", считывает числа и 
#  вычисляет их среднее значение. Выведите результат на экран.

# ls_num = []

# with open('data.txt', 'a') as file:
#     f = file.read()
#     for i in f.split():
#         j = i.replace(',', '')
#         ls_num.append(int(j))

# mid_val = round(sum(ls_num) / len(ls_num))
# print(ls_num)

# print(f'Среднее значение "{mid_val}"')


###############################################################################

#  6)Пользователь вводит список слов через пробел. Запишите этот список 
#  в файл "words.txt" с помощью пробела в качестве разделителя.

# word = input('Введите слова через пробел: ')

# with open('words.txt', 'w') as file:
#     file = file.write(' '.join(word))

###############################################################################

#  7)Создайте два файла "file1.txt" и "file2.txt" и запишите в них 
#  произвольные строки текста. Напишите программу, которая открывает 
#  оба файла, считывает их содержимое и записывает в новый файл "merged.txt"
#  содержимое обоих файлов.Тут загуглите новый метод для файлов связанный 
#  с копировкой

# with open('dz/file1.txt', 'r') as file:
#     file1 = file.read()

# with open('dz/file2.txt', 'r') as file:
#     file2 = file.read()

# merge = file1 + file2
# #print(merge)

# with open('dz/merged.txt', 'w') as file:
#      wr_file = file.write(merge)

# print(wr_file) 

###############################################################################

#8) Пользователь вводит высоту треугольника (целое число). 
#  Нарисуйте треугольник, используя символ "*". Например, для высоты 5,
#  результат должен выглядеть так:
# *
# **
# ***
# ****
# *****

# triangle = int(input('Введит высоту треугольника: '))

# for i in range(triangle):
#     print('*' * (i + 1))

###############################################################################

#  9)Пользователь вводит два слова: old_word и new_word. 
#  Откройте файл "text.txt" и замените все вхождения old_word на new_word. 
#  Сохраните изменения в файле.

# with open('dz/text.txt', 'r') as file:
#     r_file = file.read()

# new_file = r_file.split()[::-1]

# for i in new_file:
#     with open('dz/text.txt', '+a') as file:
#         w_file = file.write('\n' + i)

# print(w_file)