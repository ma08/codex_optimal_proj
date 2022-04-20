

from collections import deque

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    queue = deque([])

    for i in range(N):
        while queue and queue[-1] < A[i]:
            queue.pop()
        queue.append(A[i])
        if i >= K and queue[0] == A[i - K]:
            queue.popleft()
        if i >= K - 1:
            print(queue[0], end=' ')

if __name__ == '__main__':
    main()
