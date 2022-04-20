

import sys

def main():
    lines = sys.stdin.readlines()
    N, M = [int(x) for x in lines[0].strip().split()]
    k = [int(x) for x in lines[1:M+1]]
    s = [[int(x) for x in line.strip().split()] for line in lines[M+1:2*M+1]]
    p = [int(x) for x in lines[2*M+1].strip().split()]

    count = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            if p[j] != sum([(i>>(s[j][k]-1))&1 for k in range(k[j])])%2:
                flag = False
                break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()