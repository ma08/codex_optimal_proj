

n = int(input())
numbers = list(map(int, input().split()))

if len(numbers) == n:
    for i in range(1, n):
        if numbers[i] < numbers[i - 1]:
            numbers[i] = numbers[i - 1]

    print('Yes')
