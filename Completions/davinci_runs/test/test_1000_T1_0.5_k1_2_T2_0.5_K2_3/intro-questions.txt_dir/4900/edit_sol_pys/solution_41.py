

import sys

def main():
    n = int(sys.stdin.readline())
    distances = []
    for i in range(n):
        distances.append(list(map(int, sys.stdin.readline().split())))
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if distances[i][j] == distances[i][k] + distances[k][j]:
                    print(i+1, j+1)
                    print(i+1, k+1)
                    print(j+1, k+1)
                    return
                elif distances[i][j] == distances[i][k] - distances[j][k]:
                    print(i+1, j+1)
                    print(k+1, i+1)
                    print(i+1, k+1)
                    return
                elif distances[i][j] == distances[k][j] - distances[i][k]:
                    print(i+1, k+1)
                    print(i+1, j+1)
                    print(k+1, i+1)
                    return
                elif distances[i][j] + distances[i][k] == distances[j][k]:
                    print(j+1, k+1)
                    print(i+1, j+1)
                    print(i+1, k+1)
                    return
                elif distances[i][j] + distances[k][j] == distances[i][k]:
                    print(i+1, k+1)
                    print(j+1, k+1)
                    print(i+1, j+1)
                    return
                elif distances[i][k] + distances[j][k] == distances[i][j]:
                    print(i+1, j+1)
                    print(i+1, k+1)
                    print(j+1, k+1)
                    return

if __name__ == '__main__':
    main()
