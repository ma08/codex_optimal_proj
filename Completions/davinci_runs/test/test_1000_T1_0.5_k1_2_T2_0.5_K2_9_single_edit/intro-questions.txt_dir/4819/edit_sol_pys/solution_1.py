

modulo = 42
numbers = []
for i in range(10):
    numbers.append(int(input()) % modulo)  # you need to use input() in python 3

print(len(set(numbers)))
