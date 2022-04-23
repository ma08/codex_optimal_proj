n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    for j in range(i, n):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(' '.join(map(str, numbers)))
