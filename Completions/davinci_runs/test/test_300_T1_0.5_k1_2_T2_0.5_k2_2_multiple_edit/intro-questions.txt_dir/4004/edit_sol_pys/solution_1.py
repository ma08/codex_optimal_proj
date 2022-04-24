

def main():
    n = int(input())
    A = [int(i) for i in input().split()][:n]
    d = min(A)
    for i in range(n):
        A[i] -= d
    if sum(A) % n == 0:
        print(d)
    else:
        print(-1)

if __name__ == "__main__":
    main()
