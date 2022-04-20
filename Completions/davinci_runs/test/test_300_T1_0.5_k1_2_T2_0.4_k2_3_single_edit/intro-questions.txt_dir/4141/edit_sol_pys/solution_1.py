

def is_prime(n):
    if n == 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True

n = int(input())
num = [int(i) for i in input().split()]

for i in range(n):
    if is_prime(num[i]):
        print("DENIED")
        exit()

print("APPROVED")
