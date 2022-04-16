
import sys
import numpy as np

def main():
    N, H, L = (int(x) for x in sys.stdin.readline().split())
    horror_list = set([int(x) for x in sys.stdin.readline().split()])
    similar = np.zeros((N, N), dtype=np.int8)
    for _ in range(L):
        a, b = (int(x) for x in sys.stdin.readline().split())
        similar[a][b] = 1
        similar[b][a] = 1
    horror_index = [0] * N
    for i in range(N):
        if i in horror_list:
            continue
        horror_index[i] = np.inf
        for j in range(N):
            if similar[i][j] == 1:
                horror_index[i] = min(horror_index[i], horror_index[j] + 1)
    print(np.argmax(horror_index))

if __name__ == "__main__":
    main()
