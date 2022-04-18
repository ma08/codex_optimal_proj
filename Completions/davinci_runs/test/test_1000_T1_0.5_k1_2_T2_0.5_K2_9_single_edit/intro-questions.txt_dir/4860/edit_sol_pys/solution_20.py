

n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

for i in range(1, numbers[-1] + 1):
    if i not in numbers:
        print(i)

if len(numbers) == numbers[-1]:
    print("good job")
