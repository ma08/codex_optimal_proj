

num = float(input())

num = num * 100.0

num = int(num)

if num % 10 >= 5:
    num = num + (10 - (num % 10))

if num % 10 < 5:
    num = num - (num % 10)

num = num / 100.0

print(num)
