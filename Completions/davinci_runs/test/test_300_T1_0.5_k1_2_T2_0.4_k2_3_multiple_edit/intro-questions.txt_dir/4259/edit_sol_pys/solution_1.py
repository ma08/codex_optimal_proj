

k = int(input())
a, b = map(int, input().split())
print("OK" if a % k == 0 or b % k == 0 else "NG")
