
def search(A, d, visited):
    if sum(visited) == len(visited) - 1:
        return 1
    ret = 0
    for i in range(len(A)):
        if visited[i] == 0 and A[d][i] == 1:
            visited[i] = 1
            ret += search(A, i, visited)
            visited[i] = 0
    return ret

def main():
    n, m = map(int, input().split())
    a = [[0]*n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a[a-1][b-1] = 1
        a[b-1][a-1] = 1
    visited = [0] * n
    visited[0] = 1
    print(search(a, 0, visited))

if __name__ == '__main__':
    main()
