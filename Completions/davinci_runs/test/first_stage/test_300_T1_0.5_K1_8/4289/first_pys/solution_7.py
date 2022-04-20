

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

temp = []
for i in range(n):
    temp.append(abs(t - h[i] * 0.006 - a))

print(temp.index(min(temp)) + 1)