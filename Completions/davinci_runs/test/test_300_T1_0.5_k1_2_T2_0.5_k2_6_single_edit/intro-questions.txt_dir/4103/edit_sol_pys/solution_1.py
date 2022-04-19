


n = int(input())
s = list(map(int, input().split())

current_max = 0
current_sum = 0
for i in range(n-1):
    if s[i] <= s[i+1]:
        current_sum += 1
        current_max = max(current_max, current_sum)
    else:
        current_sum = 0

print(current_max)
