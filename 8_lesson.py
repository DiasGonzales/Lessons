# ФАЙЛЫ

# file = open(имя файла, режим доступа к файлу)

#  'r' - read() - просто чтение файла
#  'w' - write() - запись с удалением уже существующего файла
#  'a' - () - запись без удаления данных в файле в новой строке
#  'x' - создание файла если его не существует
#  'rb' - чтение в бинарном виде
#  'wb' - запись в бинарном виде


# file = open('text.txt', 'r')
# text = file.read()
# print(text)
# file.close()


# file = open('text.txt', 'w')
# text = file.write('Hello world')
# print(text)
# file.close()


# file = open('text.txt', 'a')
# text = file.write('\t Hello')
# print(text)
# file.close()


# with open('text.txt', '+a') as file:
#     text = file.write('adwdajkda')
#     print(text)
    

# with open('textss.txt', 'x') as file:    - создание нового файла
#     text = file.write('adwdajkda')


# with open('image.jpg', 'rb') as file:
#     data = file.read()
# print(data)




#############################################
"""
1)Напишите программу, которая запрашивает у пользователя ввод текста 
и сохраняет его в файл "text.txt". После записи файла программа должна 
вывести сообщение "Текст успешно записан в файл".
"""

# text = input('введите текст: ')

# with open('./text.txt', 'w') as file:
#     result = file.write(text)
# print('Текст успешно записан в файл', text)


"""
2)Создайте файл "text.txt" и запишите в него произвольный текст. 
Напишите программу, которая открывает файл "text.txt", считывает 
содержимое и подсчитывает количество слов в тексте. Выведите результат на экран.
"""

# with open('text.txt', 'r') as file:
#     text = file.read().split()

#     print(len(text))

"""
3)Создайте файл "text.txt" и запишите в него произвольный текст. 
Напишите программу, которая открывает файл "text.txt", 
считывает содержимое и подсчитывает количество символов (без учета пробелов). 
Выведите результат на экран.
"""

# with open('text.txt', 'r') as file:
#     text = file.read()

#     print(len(text.replace(" ", "")))


"""
4))Создайте файл "text.txt" и запишите в него произвольный текст. 
Напишите программу, которая открывает файл "text.txt", считывает 
содержимое и находит нужное слово в файле.
"""
# intext = input("введите текст: ")

# with open('text.txt', 'r') as file:
#     text = file.read()
# if intext in text:
#     print('вот слово:', intext)
# else:
#     print('такого слова нет')

