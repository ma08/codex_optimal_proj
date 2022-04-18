import math


n = int(input("Enter the number of measurements: "))

hours = 0
seconds = 0

for i in range(n):
    # h, m = map(int, input().split())
    h, m = (int(x) for x in input().split())
    hours += h
    seconds += m * 60

if seconds / hours > 3600:
    print("measurement error")
else:
    print(math.floor(seconds / hours))
