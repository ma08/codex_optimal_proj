lst = []
for i in range(3):
    lst.append(list(map(int, input().split())))

if lst[0][0] - lst[0][1] == lst[1][0] - lst[1][1] == lst[2][0] - lst[2][1] and lst[0][0] - lst[0][2] == lst[1][0] - lst[1][2] == lst[2][0] - lst[2][2] and lst[0][1] - lst[0][2] == lst[1][1] - lst[1][2] == lst[2][1] - lst[2][2]:
    print("Yes")
else:
    print("No")
