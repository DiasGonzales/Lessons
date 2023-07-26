
# ФУНКЦИИ

# def hello (аргумент):
#   pass #- здесь блок кода

# return # - результат 


# def hello ():
#     print("hello world")

# hello()



# ЗАДАНИЕ
# Создайте функцию, которая принимает в себя две строки: first_name и last_name и возвращает строку 
# "Привет, {имя фамилия}".

# a = (input("first_name "))
# b = (input("last_name "))

# def stroka(a: str, b: str) -> str:
#     '''''возвращает строку -> Привет 'first_name', 'last_name'''''
#     return f'Привет, {a} {b}'
# print(stroka(a, b))



# def hello (a, b): -> позиционные аргументы
#     c = a + b
#     print("hello world")

#     return c
# print(hello(2, 4))



# def hello (a=2, b=2): # именованные аргументы
#     c = a + b
#     return c
# print(hello())



#  * args,  ** kwargs

# АРГС: 

# def hello (*args):  - переменная, которая принимает в себя неограниченное количество позиционных аргументов
#     result = 0
#     for i in args:
#         result += i

#     return result
# print(hello(1, 2, 3, 4))





# КВАРГС:
 
# def hello (**kwargs): # - это аргумент, которая принимает в себя неограниченное именованных аргументов

#     for key, value in kwargs.items():
#         print(key + ':', value)

# hello(name = 'Tilek', age = '22', male = 'men')




# def hello (**kwargs):
#     for key, value in kwargs.items():
#         print(value**2)

# hello(name = 4, age = 2, male = 5)




# a = 'не хелло'

# def hello(): # пример глобального кода
#     a = "hello"
#     return a

# def ne_hello(a):
#     return a 

# print(hello())
# print(ne_hello(a))




# АНОНИМНАЯ ФУНКЦИЯ: 

# num = lambda x, y: x+y # - анонимная функция
# print(num(1, 3))



# num = lambda n : n % 2 == 0   -> проверяет четное ли число. 
# print(num(4))




# ФУНКЦИЯ РЕКУРСИЯ (вызов из самой себя)

# def fak (u):
#     if u == 0:
#         return 1
#     else:
#         return fak(u - 1) * u
# print(fak(5))


# -> это то же самое что и: 
# a = (1 * 2 * 3 * 4 * 5)
# print(a)
