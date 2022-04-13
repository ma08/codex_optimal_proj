import sys



def main():
    N, M = [int(x) for x in sys.stdin.readline().strip().split()]
    A = [int(x) for x in sys.stdin.readline().strip().split()]
    B = [int(x) for x in sys.stdin.readline().strip().split()]
    total = 0
    for i in range(N):
        total += A[i]*B[i]
    print(total)

if __name__ == "__main__":
    main()
