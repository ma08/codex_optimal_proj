

r, n = map(int, input().split())  # r: number of rooms, n: number of people

for i in range(1, r+1):  # check each room
    if i not in map(int, input().split()):
        print(i)
        break
else:
    print("too late")
