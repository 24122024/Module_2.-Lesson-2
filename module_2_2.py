# "Условная конструкция. Операторы if, elif, else"
first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second == third == first:
    print(3)
else:
    print('error')
# выводит аргумент "3", если все три целых числа равны между союой.
first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second or first == third:
    print(2)
elif second == first or second == third:
    print(2)
else:
    print('error')
# выводит аргумент "2", если 2 из 3 введёных целых чисел равны.
first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second or first == third:
    print('error')
elif second == first and second == third:
    print('error')
else:
    print(0)
# выводит аргумент "0", если равных целых чисел среди трех нет.
