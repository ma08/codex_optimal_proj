

N = int(input())
a = list(map(int, input().split()))

average = sum(a) / len(a)
diff_total = 0
for i in range(N):
    diff_total += (a[i] - average) ** 2

print(int(diff_total))
