n, m = map(int, input().split())

def countDivisible(n):
    count = 0
    for i in range(1, n):
        if i % m == 0:
            count += 1
    return count

print(countDivisible(n))
