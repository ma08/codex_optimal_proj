

k = int(input())

count = 1
num = 7

while num % k != 0:
    count += 1
    num = num * 10 + 7

print(count)