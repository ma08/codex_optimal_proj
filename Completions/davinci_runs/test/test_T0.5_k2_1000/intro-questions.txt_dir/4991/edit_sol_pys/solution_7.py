

def hailstone(n): #function to calculate the hailstone sequence
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + hailstone(n // 2)
    else:
        return n + hailstone(3*n + 1)

n = int(input())
print(hailstone(n))
