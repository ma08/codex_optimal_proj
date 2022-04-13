import sys, math

def main():
    n = int(sys.stdin.readline())
    distances = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if distances[i*n+j] == distances[i*n+k] + distances[k*n+j]:
                    print(i+1, j+1)
                    print(i+1, k+1)
                    print(j+1, k+1)
                    return
                if distances[i*n+j] == distances[i*n+k] - distances[j*n+k]:
                    print(i+1, j+1)
                    print(k+1, j+1)
                    print(i+1, k+1)
                    return
                if distances[i*n+j] == distances[k*n+j] - distances[i*n+k]:
                    print(i+1, k+1)
                    print(i+1, j+1)
                    print(k+1, j+1)
                    return
                if distances[i*n+j] + distances[i*n+k] == distances[j*n+k]:
                    print(j+1, k+1)
                    print(i+1, j+1)
                    print(i+1, k+1)
                    return
                if distances[i*n+j] + distances[k*n+j] == distances[i*n+k]:
                    print(i+1, k+1)
                    print(j+1, k+1)
                    print(i+1, j+1)
                    return
                if distances[i*n+k] + distances[j*n+k] == distances[i*n+j]:
                    print(i+1, j+1)
                    print(i+1, k+1)
                    print(j+1, k+1)
                    return

if __name__ == '__main__':
    main()
