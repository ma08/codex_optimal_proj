

# put your python code here
a, b = [int(x) for x in input().split()] # вводим число и количество знаков после запятой
a -= a % (10**b) # отнимаем остаток от деления числа на 10 в степени b
print(a) # выводим число
