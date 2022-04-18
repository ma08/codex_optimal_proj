
import queue
n = int(input())
board = [input() for _ in range(n)]

q = queue.Queue()
q.put((n-1,n-1))
visited = set()
distance = 0
while not q.empty():
    size = q.qsize()

    for _ in range(size):
        x, y = q.get()
        if (x,y) == (0,0):
            print(distance)
            exit()
        if board[x][y] == '#':
            continue
        visited.add((x,y))
        if x+1 < n and (x+1,y) not in visited:
            q.put((x+1,y))
        if x-1 >= 0 and (x-1,y) not in visited:
            q.put((x-1,y))
        if y+1 < n and (x,y+1) not in visited:
            q.put((x,y+1))
        if y-1 >= 0 and (x,y-1) not in visited:
            q.put((x,y-1))
    distance += 1
print(-1)
