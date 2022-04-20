
n, b, a = map(int, input().split())
s = list(map(int, input().split()))

max_segments = a + b
for i in range(1, n):
    if s[i] == 1 and s[i - 1] == 1:
        max_segments += 1
    else:
        max_segments += 2
print(max_segments)
