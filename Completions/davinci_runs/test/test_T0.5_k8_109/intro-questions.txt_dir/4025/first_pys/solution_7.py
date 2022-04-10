

a, b, c = map(int, input().split())

days = [0, 0, 0, 0, 0, 0, 0]
days[0] = a
days[1] = b
days[2] = c

for i in range(3, 7):
    days[i] = min(days[i-3], days[i-2], days[i-1])

print(sum(days))