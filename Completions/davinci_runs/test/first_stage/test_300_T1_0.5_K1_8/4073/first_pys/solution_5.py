

n = int(input())
arr = list(map(int, input().split(' ')))

# arr = [2, 5, 3, 1]

def find_gcd(a, b):
    if a == 0:
        return b
    return find_gcd(b % a, a)

gcd = arr[0]
for i in range(1, n):
    gcd = find_gcd(gcd, arr[i])

print(gcd)