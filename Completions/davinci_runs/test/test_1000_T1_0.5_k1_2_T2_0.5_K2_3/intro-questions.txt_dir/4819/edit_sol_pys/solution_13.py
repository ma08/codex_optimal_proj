

modulo = 42
numbers = []
for i in range(10): # 10 inputs
    numbers.append(int(input()) % modulo)

print(len(set(numbers))) # number of unique numbers
