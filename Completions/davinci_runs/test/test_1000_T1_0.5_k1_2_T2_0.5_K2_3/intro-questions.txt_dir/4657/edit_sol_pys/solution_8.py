

n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i % 2 == 1:
            if j % 2 == 1:
                print("W", end = "")
            else:
                print("B", end = "")
        else:
            if j % 2 == 1:
                print("B", end = "")
            else:
                print("W", end = "")
    print()
