

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()
    point = 0
    for i in range(N):
        point += len(A) - bisect_left(A, B[i])
    for i in range(N):
        point += len(C) - bisect_left(C, B[i])
    print(point)

if __name__ == "__main__":
    main()
