


n = int(input())
a = list(map(int, input().split()))

max_rest = 0
current_rest = 0

for i in a:
    if i == 0:
        current_rest += 1
    else:
        max_rest = max(max_rest, current_rest)
        current_rest = 0

max_rest = max(max_rest, current_rest)
print(max_rest)