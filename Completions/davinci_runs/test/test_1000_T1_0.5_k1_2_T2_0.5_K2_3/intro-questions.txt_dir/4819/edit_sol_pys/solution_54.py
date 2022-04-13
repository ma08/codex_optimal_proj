

modulo = 42
numbers = []
for i in range(10): #range(10) -> range(int(input()))
    numbers.append(int(input()) % modulo)

print(numbers)
