
N = int(input())
h_list = list(map(int, input().split()))

count = 0
for h in h_list:
    if h != 0:
        count += 1

print(count)
