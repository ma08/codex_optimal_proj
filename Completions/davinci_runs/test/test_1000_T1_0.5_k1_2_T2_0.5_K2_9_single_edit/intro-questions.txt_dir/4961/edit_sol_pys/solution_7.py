

r, c = map(int, input().split())

seats = []
for _ in range(r):
    line = input()
    seats.append(line)

# print(seats)

count = 0
for i in range(r):
    for j in range(c):
        if seats[i][j] == 'o':
            if j > 0 and seats[i][j-1] == 'o':
                count += 1
            if j < c-1 and seats[i][j+1] == 'o':
                count += 1
            if i > 0 and seats[i-1][j] == 'o':
                count += 1
            if i < r-1 and seats[i+1][j] == 'o':
                count += 1
            if i > 0 and j > 0 and seats[i-1][j-1] == 'o':
                count += 1
            if i < r-1 and j < s-1 and seats[i+1][j+1] == 'o':
                count += 1
            if i > 0 and j < c-1 and seats[i-1][j+1] == 'o':
                count += 1
            if i < r-1 and j > 0 and j < c-1 and seats[i+1][j-1] == 'o':
                count += 1

print(count)
