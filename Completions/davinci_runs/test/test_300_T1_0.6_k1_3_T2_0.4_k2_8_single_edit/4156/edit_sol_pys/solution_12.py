

n, w = map(int, input().split())  # n = number of stops, w = maximum number of passengers
a = list(map(int, input().split()))  # list of passengers getting on at each stop

min_passengers = max_passengers = 0
for i in range(n):
    max_passengers += a[i]
    min_passengers = max(min(min_passengers+a[i], 0), max_passengers)

if max_passengers > w:
    print(0)
else:
    print(w-max_passengers+1-min_passengers)
