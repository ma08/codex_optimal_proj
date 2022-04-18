import sys

def main():
    N, K = [int(i) for i in sys.stdin.readline().split()]
    D = [int(i) for i in sys.stdin.readline().split()]
    D.sort()
    i = 0
    count = 0
    while i < N:
        count += 1
        j = i + 1
        while j < N and D[j] - D[i] <= K:
            j += 1
        i = j
    print(count)

if __name__ == '__main__':
    main()
