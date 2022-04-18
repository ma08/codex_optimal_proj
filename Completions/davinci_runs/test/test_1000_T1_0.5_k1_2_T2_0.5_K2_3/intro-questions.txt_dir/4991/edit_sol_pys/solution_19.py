

def hailstone(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

n = int(input())
print(hailstone(n))
