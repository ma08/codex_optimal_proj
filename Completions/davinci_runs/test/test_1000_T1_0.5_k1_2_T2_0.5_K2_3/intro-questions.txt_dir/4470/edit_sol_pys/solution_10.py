

def calculate(n):
    if n == 1:
        return 0

    elif n % 2 == 0:
        return 1 + calculate(n/2)
    elif n % 3 == 0:
        return 1 + calculate(2*n/3)
    elif n % 5 == 0:
        return 1 + calculate(4*n/5)
    return -1

q = int(input())

for i in range(q):
    n = int(input())
    print(calculate(n))
