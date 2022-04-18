

def main():
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] //= 2
            cnt += 1

n = int(input())
t, a = map(int, input().split())
h = [int(input()) for i in range(n)]

diff = []
for i in range(n):
    diff.append(abs(t - h[i] * 0.006 - a))

print(diff.index(min(diff)) + 1)
