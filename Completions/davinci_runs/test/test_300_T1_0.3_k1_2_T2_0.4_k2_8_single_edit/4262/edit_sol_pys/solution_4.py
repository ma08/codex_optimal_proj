

import sys

def main():
    n = int(input())
    p = list(map(int, input().split())) + [1000000]
    q = list(map(int, input().split())) + [1000000]
    p_index = 0
    q_index = 0
    for i in range(n):
        if p[i] > p[i+1]:
            p_index = i
        if q[i] > q[i+1]:
            q_index = i
    print(abs(p_index - q_index))

if __name__ == '__main__':
    main()
