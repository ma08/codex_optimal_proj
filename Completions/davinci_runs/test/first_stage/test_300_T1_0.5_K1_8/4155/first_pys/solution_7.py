

N = input()
h = list(map(int, input().split()))

watering_operation = 0
for i in range(N):
    if h[i] == 0:
        continue
    watering_operation += 1
    for j in range(i, N):
        if h[j] > 0:
            h[j] -= 1
        else:
            break

print(watering_operation)