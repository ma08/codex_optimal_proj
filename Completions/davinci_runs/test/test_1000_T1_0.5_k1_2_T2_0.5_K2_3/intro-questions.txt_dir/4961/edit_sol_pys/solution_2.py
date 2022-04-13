
r, s = map(int, input().split())

seats = []
for _ in range(r):
    line = input()
    seats.append(line)

count = 0
    if i > 0:
        if seats[i-1][j] == 'o':
            count += 1
            if j > 0 and seats[i-1][j-1] == 'o':
                count += 1
            if j < s-1 and seats[i-1][j+1] == 'o':
                count += 1
for i in range(r):
    for j in range(s):
        if seats[i][j] == 'o':
            if j > 0 and seats[i][j-1] == '.':
                count += 2
            if j < s-1 and seats[i][j+1] == '.':
                count += 2
            if i < r-1 and seats[i+1][j] == '.':
                count += 2
            if i < r-1 and j > 0 and seats[i+1][j-1] == '.':
                count += 2
            if i < r-1 and j < s-1 and seats[i+1][j+1] == '.':
                count += 2

print(count)
