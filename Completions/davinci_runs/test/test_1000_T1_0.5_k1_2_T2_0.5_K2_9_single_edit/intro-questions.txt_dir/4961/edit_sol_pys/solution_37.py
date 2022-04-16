r, s = [int(i) for i in input().split()]

matrix = []
for _ in range(r):
    matrix.append(input())
handshakes = 0
for i in range(r):
    for j in range(s):
        if matrix[i][j] == 'o':
            if i > 0 and matrix[i-1][j] == 'o':
                handshakes += 1
            if i < r - 1 and matrix[i+1][j] == 'o':
                handshakes += 1
            if j > 0 and matrix[i][j-1] == 'o':
                handshakes += 1
            if j < s - 1 and matrix[i][j+1] == 'o':
                handshakes += 1
            if i > 0 and j > 0 and matrix[i-1][j-1] == 'o':
                handshakes += 1
            if i > 0 and j < s - 1 and matrix[i-1][j+1] == 'o':
                handshakes += 1
            if i < r - 1 and j > 0 and matrix[i+1][j-1] == 'o':
                handshakes += 1
            if i < r - 1 and j < s - 1 and matrix[i+1][j+1] == 'o':
                handshakes += 1
print(handshakes)
