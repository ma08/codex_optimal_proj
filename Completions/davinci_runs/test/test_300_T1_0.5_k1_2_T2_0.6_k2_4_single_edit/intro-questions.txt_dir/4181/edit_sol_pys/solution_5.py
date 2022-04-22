import sys

def main():
    N = int(sys.stdin.readline())
    A = [int(x) for x in sys.stdin.readline().split(' ')]
    B = [int(x) for x in sys.stdin.readline().split(' ')]

    answer = 0
    for i in range(N):
        answer += min(A[i], B[i])
        answer += min(A[i+1], B[i])

    print(answer)

if __name__ == '__main__':
    main()
