
r, c = map(int, input().split())
parking = [input() for _ in range(r)]

squash = [0, 0, 0, 0, 0]
for i in range(r-1):
    for j in range(c-1):
        if parking[i][j] == "#":
            continue
        elif parking[i][j] == ".":
            if parking[i+1][j] == "X" and parking[i][j+1] == "X" and parking[i+1][j+1] == "X":
                squash[4] += 1
            elif parking[i+1][j] == "X" and parking[i][j+1] == "X":
                squash[3] += 1
            elif parking[i+1][j] == "X" and parking[i+1][j+1] == "X":
                squash[3] += 1
            elif parking[i][j+1] == "X" and parking[i+1][j+1] == "X":
                squash[3] += 1
            elif parking[i+1][j] == "X":
                squash[2] += 1
            elif parking[i][j+1] == "X":
                squash[2] += 1
            elif parking[i+1][j+1] == "X":
                squash[2] += 1
            else:
                squash[0] += 1
        else:
            squash[1] += 1

print(squash[0])
print(squash[1])
print(squash[2])
print(squash[3])
print(squash[4])
