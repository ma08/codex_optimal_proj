
s = input()  # строка, которую нужно проверить
t = input()  # строка, которая используется для проверки
correct = 0  # количество правильных ответов

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
