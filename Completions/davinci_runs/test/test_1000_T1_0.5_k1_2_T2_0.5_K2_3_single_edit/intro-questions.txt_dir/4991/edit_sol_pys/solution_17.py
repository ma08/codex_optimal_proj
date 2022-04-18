

def hailstone(n):
    if n == 1:
        return 1
    if n % 2 != 0:
        return n + hailstone(3 * n + 1)
    return n + hailstone(n // 2)


n = int(input())
print(hailstone(n))
