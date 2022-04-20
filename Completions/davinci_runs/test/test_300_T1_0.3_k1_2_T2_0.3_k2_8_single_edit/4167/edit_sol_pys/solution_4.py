
import numpy as np

def main():
    N = int(input())
    A = np.array(list(map(int, input().split())))
    B = np.array(list(map(int, input().split())))
    C = np.array(list(map(int, input().split())))
    A_sort = np.sort(A)
    C_sort = np.sort(C)
    ans = 0
    for b in B:
        ans += np.searchsorted(A_sort, b) * (N - np.searchsorted(C_sort, b, side='right'))
    print(ans)

if __name__ == '__main__':
    main()
