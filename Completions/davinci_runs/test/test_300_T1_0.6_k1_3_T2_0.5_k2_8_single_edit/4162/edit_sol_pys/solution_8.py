import sys
from collections import deque




def main():
    input = sys.stdin.readline()
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = deque(map(int, input().split()))
    C = deque()
    for i in range(M):
        if len(B) == 0:
            break
        if len(C) < N:
            if B[0] <= A[0]:
                C.append(B.popleft())
            else:
                C.append(A.pop(0))
        else:
            if B[0] > C[0]:
                C.append(B.popleft())
                C.popleft()
            else:
                C.append(A.pop(0))
                C.popleft()
    print(sum(C))


if __name__ == '__main__':
    main()
