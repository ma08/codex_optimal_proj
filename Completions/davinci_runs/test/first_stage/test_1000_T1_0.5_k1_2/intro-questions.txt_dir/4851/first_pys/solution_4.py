

n = int(input())

while True:
    n += 1
    if n % sum([int(i) for i in str(n)]) == 0:
        print(n)
        break