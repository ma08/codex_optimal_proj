

def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

q = int(input())

for i in range(q):
    n = int(input())
    if isprime(n):
        print("YES")
    else:
        print("NO")
