

input_str = input()  # вводим строку 

is_palindrome = True  # предполагаем, что строка является палиндромом
for i in range(int(len(input_str) / 2)):  # для каждого символа в строке
    if input_str[i] != input_str[-i - 1]:  # сравниваем символ с противоположным ему
        is_palindrome = False  # если символы не совпали, то строка не является палиндромом

if is_palindrome:
    print('Yes')
else:
    print('No')
