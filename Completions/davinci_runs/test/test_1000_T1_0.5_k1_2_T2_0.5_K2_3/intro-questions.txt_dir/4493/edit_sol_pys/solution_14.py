
lst = []
for i in range(3):
    lst.append(list(map(int, input().split())))

for a1 in range(0, 101):  # 0 <= a1 <= 100
    for a2 in range(0, 101):  # 0 <= a2 <= 100
        for a3 in range(0, 101):  # 0 <= a3 <= 100
            for b1 in range(0, 101):  # 0 <= b1 <= 100
                for b2 in range(0, 101):  # 0 <= b2 <= 100
                    for b3 in range(0, 101):  # 0 <= b3 <= 100
                        if lst[0][0] == a1 + b1 and lst[0][1] == a2 + b2 and lst[0][2] == a3 + b3 and lst[1][0] == a1 + b1 and lst[1][1] == a2 + b2 and lst[1][2] == a3 + b3 and lst[2][0] == a1 + b1 and lst[2][1] == a2 + b2 and lst[2][2] == a3 + b3:  # a1 + b1 = a2 + b2 = a3 + b3
                            print('Yes')
                            exit(0)
print("No")
