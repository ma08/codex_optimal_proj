

def main():
    n = int(input())
    A = list(map(int, input().split()))
    D = min(A)
    A = [i-D for i in A]
    if sum(A) % n == 0:
        print(D)
    else:
        print(-1)

if __name__ == "__main__":
    main()
