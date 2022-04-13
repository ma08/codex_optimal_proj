

def hailstone(n): 
    if n != 1:
        if n % 2 == 0:
            return n + hailstone(n/2)
        else:
            return n + hailstone(3*n + 1)
    else:
        return 1

n = int(input())
print(hailstone(n))
