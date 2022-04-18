t = int(input())  # num of test cases
for _ in range(t):
    a, b, k = map(int, input().split())  # a, b, k
    if k % 2 == 0:
        print(k // 2 * (a - b))  # k is even
    else:
        print(k // 2 * (a - b) + a)  # k is odd
