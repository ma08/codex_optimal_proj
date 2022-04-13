

input_line = input().split()
r = int(input_line[0])
n = int(input_line[1])

booked = set()
for i in range(n):
    booked.add(int(input()))

for i in range(1, r+1):
    if i not in booked:
        print(i)
        break
else:
    print("too late")
