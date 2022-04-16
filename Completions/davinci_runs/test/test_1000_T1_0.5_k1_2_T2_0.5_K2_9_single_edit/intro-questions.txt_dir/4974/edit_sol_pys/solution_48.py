
input_line = input().split()
r = int(input_line[0])
n = int(input_line[1])

booked = set()
for i in range(n):
    booked.add(int(input()))

for room in range(1, r+1):
    if room not in booked:
        print(room)
        break
else:
    print("too late")
