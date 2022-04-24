from collections import deque


def solve(n):
    q = deque([])
    q.append(n)
    cnt = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node == 2:
                return cnt
            if node % 3 == 0:
                q.append(node // 3)
            if node % 2 == 0:
                q.append(node // 2)
            q.append(node - 1)
        cnt += 1
    return cnt


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
