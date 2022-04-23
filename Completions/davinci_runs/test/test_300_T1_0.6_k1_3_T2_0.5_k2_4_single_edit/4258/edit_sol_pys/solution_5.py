
a, b, t = map(int, input().split())

total_biscuits = 0
time = 0
while time <= t:
    total_biscuits += b
    time += a

print(total_biscuits)
