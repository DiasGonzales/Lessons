# # ОПЕРАТОР IF ELSE

# x = 4




# if x < 3:   #  <>  ==  !=   or  and  not   in
#     print("yes")
# else:
#     print("no")


# if x == 4: - # равен
#     print("yes")



# if x != 4:  - # не равен
#     print("yes")
# else:
#     print("yes too")




# if x == 4 or x > 5:  #  срабатывает если хотя бы одно условие TRUE
#     print("yes")
# else:
#     print("no")


# if x == 4 and x > 5: -  #  несрабатывает если хотя бы одно условие FALSE 
#     print("yes")
# else:
#     print("no") - будет NO



# if x == 4 and x > 5 or x > 100: -  #  срабатывает читая слева направо, то есть оператор AND
#     print("yes")
# else:
#     print("no")



# b = [4, 5, 3, 7]
# v = -4 



# if x in b:  # - проверяет находится переменная х в списке и выдает True или False
#     print("yes")
# else:
#     print("no")



# # if x < 3:       # -   
#     print("yes")
# elif x == 3:
#     print("mb")
# else:
#     x > 3
#     print("no")
 


# if not x == 4:  # - видоизменяет логику IF (IF становится FALSE,  FALSE становится IF)
#     print("yes")
# else:
#     print("no")






# Есть список пользователей которые находятся в списке :
# username = [‘hasan001’, ’pro100_tilek_kg’,  ’mega_baku’, ‘killer_Aidai’], 
# нужно чтобы вы просили пользователя ввести никнейм и программа проверяла , 
# занят ли этот никнейм, если да то писал об этом , если нет то добавлял его в список и писал об этом.

# username = ['hasan001', 'pro100_tilek_kg',  'mega_baku', 'killer_Aidai']

# a = input('Введите никнейм:  ')

# if a in username:
#     print('никнейм занят')
# else:
#     username.append(a)
#     print('никнейм добавлен')
#     print(username)


# 2
# Напишите программу, которая принимает от пользователя два числа и выводит их сумму, 
# только если оба числа положительные. В противном случае, выводится сообщение об ошибке.

# a = int(input())
# b = int(input())

# if a > 0 and b > 0:
#     print('сумма этих чисел:', a + b)
# else:
#     print("Ошибка")


# 3
    # Напишите программу, которая принимает число от пользователя и 
    # выводит сообщение "Число четное", если число четное, и "Число нечетное", 
    # если число нечетное.

# a = int(input())

# if a % 2 == 0:
#     print("число четное")
# else:
#     print("число нечетное")


# 4

# Напишите программу, которая принимает строку от пользователя и проверяет, 
# является ли она палиндромом (читается одинаково слева направо и справа налево).


# [0:2:-1]


# word = input("Word : ")
# pal_word = word[::-1]

# if word == pal_word:
#     print('PALINDORM')
# else:
#     print('NOT PAL')

