#print('hello world')
#a = 123
#b = 1.23
#print(a)  #вывод
#print(b)
#print(type(a))  #type - узнать тип переменной
#print(type(b))
#value = None
#value = 1234
#print(type(value))
#s = 'hello world'
#print(s)  #вывод строки

# s = 'hello \nworld' # \n - вывод с переходом на новую строку
# print(s, a, b) #первый  вид вывода
# print(s, '-', a, '-', b) #второй  вид вывода
# print('{} - {} - {}'. format(s, a, b))#третий вид вывода
# print(f'{a} - {b} - {s}') #четвертый вид интерполяция
# print('{2} - {1} - {0}'. format(s, a, b)) #вывод исходя из индекса выводимых данных
# f = False
# print(f)

# list = []  # описание и вывод массива(его подобие) массива
# print(list)
# list = [1,2,3]  # описание и вывод массива(его подобие) массива
# print(list)
# list = ['1','2','hello world']  # описание и вывод массива(его подобие) массива
# print(list)
# list = ['1','2','hello world', 1, 2, 4.5, True]  # можно выводить данные разных типов(строкиб целочисленныеб вещественные, логические)
# print(list)

# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print('{} - {}'. format(a, b)) # ввод данных через input

# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+', b, '=', a+b) # операция сложения для целочисленных выражений

# print('Введите а')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, '+', b, '=', a+b) # операция сложения для вещественных чисел 

# a = 30
# b = 6
# c = a//b # // два раза деление означает деление с выводом целого числа:например 12/8 = 1,5 и 12//8=1
# print(c)

# a = 30
# b = 13
# c = a%b # % операция выдающая остаток от деления
# print(c)

# a = 2
# b = 3
# c = a**b # ** возведение первого числа в степень второго числа: 2 в 3степени
# print(c)

# a = 1.52364
# b = 3
# c = round(a*b, 3) #round(a * b, 3) округление цифр после запятой. Число 3 количество цифр полсе запятой
# print(c)

# a = 2
# a += 5  # a += 5 соответсвтует a = a+5
# print(a)

# a = 2 > 1 and 5<3 # логические операции > больше < меньше, and - можно сравнивать несколько выражений
# print(a)

# a = 1 !=2 # логические операции : != - не равно
# print(a)

# a = 'abc' 
# b = 'abc' # можно сравнивать строчные выражения. == это знак равенства между выражениями. Результат либо True либо False
# print(a == b)

# a = [1,2] 
# b = [1,2,3] # можно сравнивать строчные выражения. == это знак равенства между выражениями. Результат либо True либо False
# print(a == b)

# func = 1
# t = 4
# x = 123
# print(func<t>x)  # можно и такие неравенства

# f = 1>2 or 4<6
# print(f)

# f = [1,2,3,4] 
# print(f)
# print(2 in f) # то есть цифра 2 находится в списке цифр 1,2,3,4

# f = [1,2,3,4] 
# print(f)
# print(not 2 in f) # то есть цифра 2 не находится в списке цифр 1,2,3,4

# is_odd = f[0] % 2 == 0
# print(is_odd)  # f[0] - нулевой элемент списка [1,2,3,4] то есть число 1

# is_odd = not f[0] % 2
# print(is_odd) # предыдущее выражение только в другой записи

# a = int(input('a = '))
# b = int(input('b = '))
# if a>b:
#     print(a)
# else:
#     print(b) # оператор if & else

# username = input ('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)  # цикл while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)  # цикл while и else

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i**2) # цикл for

# r = range(1, 5)
# for i in r:
#     print(i) # показывает числа от 0 до указанного числа в скобках (10), либо в диапазоне: range(1,10)

# r = range(1, 5, 2)
# for i in r:
#     print(i) # показывает числа с приращением третьего числа к каждому числу диапазона ,
    # но если число будет больше крайнего числа диапазона то не будет отражено

#help(isinstance)    # спрака о том что делает та или иная функция. В скобках нужно указать функцию

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return   
# arg = 2
# print (f(arg))    
# print (type(f(arg)) )      # функция
