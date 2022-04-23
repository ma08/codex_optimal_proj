

input_str = input() # Ввод строки

is_palindrome = True # Присваиваем переменной значение True
for i in range(int(len(input_str) / 2)): # Обходим все элементы строки
    if input_str[i] != input_str[-i - 1]: # Если первый элемент не равен последнему
        is_palindrome = False # Присваиваем переменной значение False

if is_palindrome:
    print('Yes')
else:
    print('No')
