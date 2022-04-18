

    from collections import deque
    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue.append((0, 0, 0))
    visited[0][0] = True
    while queue:
        i, j, dist = queue.popleft()
        if i == n - 1 and j == n - 1:
            return dist
        for x, y in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
            if 0 <= x < n and 0 <= y < n and not visited[x][y] and mat[x][y] > k:
                queue.append((x, y, dist + 1))
                visited[x][y] = True
def get_min_dist(n, k, mat):
    # Implement your solution here


if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    mat = []
    for i in range(n):
        mat.append([int(x) for x in input().split()])
    print(get_min_dist(n, k, mat))  #
