
modulo = 10
numbers = []
for i in range(10):
    numbers.append(int(input()) % modulo)

print(numbers.count(0))
