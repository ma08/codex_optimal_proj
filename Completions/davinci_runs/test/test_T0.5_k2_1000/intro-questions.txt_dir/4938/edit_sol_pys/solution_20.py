

x = int(input())  # количество разрешенных отклонений
s = input()

w = 0  # количество девочек
m = 0  # количество мальчиков
i = 0  # количество проверок

for c in s:
    if c == 'W':
        w += 1
    else:
        m += 1
    if abs(w - m) > x:
        break
    i += 1

print(i)
