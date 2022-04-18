

input_n = int(input())  # число записей в файле
input_s = input()  # строка для подсчета

max_count = 0  # максимальное кол-во повторений
max_gram = ""  # грамма с максимальным кол-вом повторений
for i in range(input_n - 1):
    gram = input_s[i:i + 2]  # подстрока длиной 2 символа
    if input_s.count(gram) > max_count:  # если кол-во повторений больше максимального
        max_count = input_s.count(gram)  # записываем его как максимальное
        max_gram = gram  # и записываем грамму
print(max_gram)  # выводим грамму
