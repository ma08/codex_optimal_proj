
def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    D = min(A)
    a = sum([a - D for a in A])
    if a % n == 0:
        print(D)
    else:
        print(-1)

if __name__ == "__main__":
    main()
