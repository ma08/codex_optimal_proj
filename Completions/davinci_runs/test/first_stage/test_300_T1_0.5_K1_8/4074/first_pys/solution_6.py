

# Solution

num_tests = int(input())

for _ in range(num_tests):
    n, k = [int(x) for x in input().split()]
    print(n // k + int(n % k != 0))