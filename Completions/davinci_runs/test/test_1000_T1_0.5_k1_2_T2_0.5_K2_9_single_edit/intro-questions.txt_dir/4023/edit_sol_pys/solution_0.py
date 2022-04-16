

n = int(input())
a = list(map(int, input().split()))

if a.count(a[0]) == n:
    print("YES")
    exit()

a_sorted = sorted(a)

for i in range(n - 1):
    if a_sorted[i] + 1 != a_sorted[i + 1]:
        print("NO")
        exit()


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def the_number_of_prime_numbers(n):
    count = 0
    for i in range(n):
        if is_prime(i):
            count += 1
    return count
print("YES")
