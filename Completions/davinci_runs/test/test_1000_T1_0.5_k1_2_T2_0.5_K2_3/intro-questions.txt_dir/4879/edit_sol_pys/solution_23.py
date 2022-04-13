import sys

a, b, c = sys.stdin.read().split() # Вводим данные

if (a == "North" and (b == "West" and c == "East" or b == "East" and c == "West")) or \ # Сравниваем значения
        (a == "South" and (b == "West" and c == "East" or b == "East" and c == "West")) or \ # Сравниваем значения
        (a == "East" and (b == "North" and c == "South" or b == "South" and c == "North")) or \ # Сравниваем значения
        (a == "West" and (b == "North" and c == "South" or b == "South" and c == "North")): # Сравниваем значения
    print("Yes") # Выводим результат
else:
    print("No") # Выводим результат
