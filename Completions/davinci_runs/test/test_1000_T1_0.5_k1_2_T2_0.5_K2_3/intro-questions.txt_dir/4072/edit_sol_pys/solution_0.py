
# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.
# Пример:
# s = "abababa"
# t = "aba"
# Вхождения строки t в строку s:
# abababa
# abababa
# abababa
# Результат:
# 3
s = input()
t = input()
count = 0
for i in range(0, len(s)):
    if s[i:i+len(t)] == t:
        count += 1
print(count)
