
n = int(input())
modulo = 42
numbers = []
for i in range(n):
    numbers.append(int(input()) % modulo)

print(len(set(numbers)))
