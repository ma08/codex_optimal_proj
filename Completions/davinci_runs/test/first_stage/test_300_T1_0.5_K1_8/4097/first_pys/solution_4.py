

n = int(input())
b = list(map(int, input().split()))

# check if already arithmetic progression
if len(set(b)) <= 2:
    print(0)
    exit()

# check if already arithmetic progression
if len(set(b)) == 3:
    print(1)
    exit()

# check if already arithmetic progression
if len(set(b)) == 4:
    if b[0] == b[1] and b[0] != b[2]:
        print(1)
        exit()
    if b[3] == b[4] and b[3] != b[2]:
        print(1)
        exit()
    if b[1] == b[2] and b[0] != b[1]:
        print(1)
        exit()
    if b[2] == b[3] and b[3] != b[4]:
        print(1)
        exit()

# check if already arithmetic progression
if len(set(b)) == 5:
    if b[0] == b[1] and b[0] != b[2] and b[3] == b[4]:
        print(2)
        exit()
    if b[0] == b[1] and b[0] != b[2] and b[2] == b[3]:
        print(2)
        exit()
    if b[1] == b[2] and b[0] != b[1] and b[3] == b[4]:
        print(2)
        exit()
    if b[1] == b[2] and b[0] != b[1] and b[2] == b[3]:
        print(2)
        exit()
    if b[2] == b[3] and b[3] != b[4] and b[0] == b[1]:
        print(2)
        exit()
    if b[2] == b[3] and b[3] != b[4] and b[1] == b[2]:
        print(2)
        exit()
    if b[3] == b[4] and b[3] != b[2] and b[0] == b[1]:
        print(2)
        exit()
    if b[3] == b[4] and b[3] != b[2] and b[1] == b[2]:
        print(2)
        exit()

print(-1)