

N, L = map(int, input().split())

drawers = [[] for _ in range(L)]

for i in range(N):
    A, B = map(int, input().split())
    drawers[A-1].append(i)
    drawers[B-1].append(i)

visited = [False] * N
stored = [False] * N

def move(i, drawer):
    while drawers[drawer-1] != []:
        previous = drawers[drawer-1][-1]
        if visited[previous]:
            return False
        visited[previous] = True
        drawer = A[previous] if drawer == B[previous] else B[previous]
    return True

for i in range(N):
    if stored[i]:
        continue
    if drawers[A[i]-1] == []:
        stored[i] = True
        continue
    if drawers[B[i]-1] == []:
        stored[i] = True
        continue
    visited[i] = True
    if move(i, A[i]):
        stored[i] = True
        continue
    if move(i, B[i]):
        stored[i] = True
        continue

for i in range(N):
    if stored[i]:
        print("LADICA")
    else:
        print("SMECE")