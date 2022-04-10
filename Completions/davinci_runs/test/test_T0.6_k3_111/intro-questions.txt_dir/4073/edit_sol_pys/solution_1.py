
def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(n - A.count(A[0]))

if __name__ == "__main__":
    main()
