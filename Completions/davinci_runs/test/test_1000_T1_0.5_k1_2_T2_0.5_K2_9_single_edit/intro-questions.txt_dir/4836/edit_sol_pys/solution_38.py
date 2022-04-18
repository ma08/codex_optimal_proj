

N, C = map(int, input().split())
w = list(map(int, input().split()))

count = 0

while C > 0:
    if w[count] <= C:
        C -= w[count]
        count += 1
    else:
        break

print(count)
