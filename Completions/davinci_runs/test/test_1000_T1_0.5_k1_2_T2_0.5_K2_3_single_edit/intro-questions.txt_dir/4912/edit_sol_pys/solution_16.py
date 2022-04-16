

# n = int(input("Введите количество чисел: "))
#
# s = 0
#
# for i in range(n):
#     s += int(input("Введите число: "))
#
# if s % n == 0:
#     print('YES')
# else:
#     print('NO')

n = int(input("Введите количество чисел: "))

s = 0

for i in range(n):
    s += int(input("Введите число: "))

if s % n == 0:
    print('YES')
else:
    print('NO')
