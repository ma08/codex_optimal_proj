
def is_prime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return 0
    return 1

test_case = int(input())
for _ in range(test_case):
    a = input()
    if is_prime(int(a)):
        print(a)
    else:
        print(int(a[::-1]))
