

r, n = [int(x) for x in input().split()]  # Get number of rooms and number of booked rooms
booked = set()
for _ in range(n):
    booked.add(int(input()))  # Get set of booked rooms
for i in range(1, r+1):
    if i not in booked:
        print(i)
        break
else:
    print("too late")
