
r, n = [int(x) for x in input().split()]  # number of rooms and number of booked rooms
booked = set()
for _ in range(n):
    booked.add(int(input()))  # add booked rooms to set
for i in range(1, r+1):
    if i not in booked:
        print(i)
        break
else:
    print("too late")
