
#программа выводит последовательность чисел фибоначчи
k = int(input())

fib_1 = 0
fib_2 = 1

for i in range(k):
    fib_1, fib_2 = fib_2, fib_1+fib_2

print(fib_1, fib_2)
