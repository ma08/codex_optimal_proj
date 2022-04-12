
M, N, C = input().split()
M = int(M)
N = int(N)

frame1 = [input() for _ in range(M)]
input()
frame2 = [input() for _ in range(M)]

def findFalcon(frame, c):
    for i in range(M) :
        for j in range(N) :
            if frame[i][j] == c:
                return i, j

def shift(frame1, frame2, c):
    x1, y1 = findFalcon(frame1, c)
    x2, y2 = findFalcon(frame2, c)
    return x1 - x2, y1 - y2

def shiftFrame(frame, dx, dy):
    return [frame[i][:dy] + ' '*(N - dy) for i in range(M - dx)] + [''] * dx

def solve(frame1, frame2, c):
    dx, dy = shift(frame1, frame2, c)
    shiftedFrame1 = shiftFrame(frame1, dx, dy)
    shiftedFrame2 = shiftFrame(frame2, dx, dy)
    for i in range(M) :
        for j in range(N) :
            if frame2[i][j] == c:
                shiftedFrame1[i] = shiftedFrame1[i][:j] + c + shiftedFrame1[i][j+1:]
    return shiftedFrame1

print('\n'.join(solve(frame1, frame2, C)))
print()
