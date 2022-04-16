

mod = 42
numbers = []
for i in range(10):
    numbers.append(int(input()) % mod)

print(len(set(numbers)))
