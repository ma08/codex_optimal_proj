
lst = []
for i in range(3):
    lst.append(list(map(int, input().split())))

for a in range(101):
    for b in range(101):
        if lst[0][0] == a + b and lst[0][1] == a + b and lst[0][2] == a + b and lst[1][0] == a + b and lst[1][1] == a + b and lst[1][2] == a + b and lst[2][0] == a + b and lst[2][1] == a + b and lst[2][2] == a + b:
            print("Yes")
            exit()
print("No")
