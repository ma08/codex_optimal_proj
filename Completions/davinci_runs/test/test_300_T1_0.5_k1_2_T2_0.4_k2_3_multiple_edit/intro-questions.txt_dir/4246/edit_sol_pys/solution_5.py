

s = input()  # Строка, которую нужно проверить
t = input()  # Строка, которая используется для проверки

correct = 0  # Количество правильных ответов

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
