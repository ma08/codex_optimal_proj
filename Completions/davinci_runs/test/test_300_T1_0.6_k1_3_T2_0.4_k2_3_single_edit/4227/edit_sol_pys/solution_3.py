

def search(A, d, visited, N):
    if sum(visited) == len(visited):
        return 1
    ret = 0
    for i in range(N):
        if visited[i] == 0 and A[d][i] == 1:
            visited[i] = 1
            ret += search(A, i, visited, N)
            visited[i] = 0
    return ret

def main():
    N, M = map(int, input().split())
    A = [[0]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        A[a-1][b-1] = 1
        A[b-1][a-1] = 1
    visited = [0] * N
    visited[0] = 1
    print(search(A, 0, visited, N))

if __name__ == '__main__':
    main()
