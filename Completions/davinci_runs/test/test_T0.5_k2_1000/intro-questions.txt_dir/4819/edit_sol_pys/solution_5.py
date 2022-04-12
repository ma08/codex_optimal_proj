
modulo = 10
numbers = []
for i in range(5):
    numbers.append(int(input()) % modulo)

print(len(set(numbers)))
