n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    if a == b or c == d or a == c or b == d or a == d or b == c:
        print(a, b)
        continue
    print(a, c)
