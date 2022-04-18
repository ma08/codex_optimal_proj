

def hailstone(n):
    if n == 0:
        return 1
    elif n % 3 == 0:
        return n + hailstone(n/3)
    else:
        return n + hailstone(2*n + 1)

n = int(input())
print(hailstone(n))
