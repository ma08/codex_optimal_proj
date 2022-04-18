
N = int(input())
a = list(map(int, input().split()))
odd_count = 0
for i in range(N):
    if a[i] % 2 == 1:
        odd_count += 1
if odd_count % 2 == 0:
    print("Yes")
else:
    print("No")
