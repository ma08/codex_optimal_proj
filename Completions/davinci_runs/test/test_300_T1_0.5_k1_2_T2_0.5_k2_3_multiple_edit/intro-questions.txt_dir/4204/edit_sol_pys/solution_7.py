
s = input()  # ввод числа
k = int(input())  # ввод номера цифры

for i in range(15):  # замена цифр на несколько цифр
    s = s.replace("2", "22")
    s = s.replace("3", "333")
    s = s.replace("4", "4444")
    s = s.replace("5", "55555")
    s = s.replace("6", "666666")
    s = s.replace("7", "7777777")
    s = s.replace("8", "88888888")
    s = s.replace("9", "999999999")

print(s[k-1])  # вывод цифры по номеру
