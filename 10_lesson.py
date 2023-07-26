# ДЕКОРАТОРЫ:
    
# def my_decorator(func):
#     def wrapper():
#         print('до вызова функции')
        
#         func()
        
#         print('После вызова функции')
          
#     return wrapper

# @my_decorator
# def hello():
#     print('привет, это между вызовами')
    
# hello()




# Примеры декоратора с аргументами: 

# def in_num(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#                 return result
#             return wrapper
#         return decorator
    
# @in_num(5)
# def hello (name):
#     print('hello', name)

# hello('Tilek')


# @classmethod
# @property
# @staticmethod





# def typecheck(x=int, y=str):
#     def decorator(func):
#             result = func()
#             return result
#     return decorator
    
# @typecheck(5, 'Tilek')
# def hello (name):
#     print('hello')

# print(hello)





# def my_sqr(value) -> int:
#     def decorator(func):
#             result = func()
#             return result
#     return decorator
    
# @my_sqr(str)
# def hello ():
#     print(my_sqr)

# print(hello)



###############################################################
# Задача: Проверка аргументов функции.
# Напишите декоратор который проверяет аргументы функции на тип 
# и выводит предупреждение, если они не соответствуют ожидаемым типам. 
# Пусть функция принимает два аргумента: x (целое число) и y (строка). 
# Если типы аргументов не соответствуют ожидаемым, выведите предупреждение 
# на экран.



# def decorator(func):
#     def wrapper(x, y):
#         if not isinstance(x, int):
#             print('х не соответствует, должно быть число')
#         else:
#             print('правильно')
#         if not isinstance(y, str):
#             print('у не соответствует, должна быть строка')
#         return func(x, y)
#     return wrapper
    
# @decorator
# def example(x, y):
#     pass

# example(5, "hello")
# example("hello", "hello2")


    



