
n = int(input())
a, b, c, d, e = [int(i) for i in input().split()]

def minute_needed(n):
    return (n + a - 1) // a + (n + b - 1) // b + (n + c - 1) // c + (n + d - 1) // d + (n + e - 1) // e

print(minute_needed(N))
