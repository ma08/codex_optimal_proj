

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == 1 or A[0] == 2:
        print(n)
    else:
        print(n - 1)

if __name__ == "__main__":
    main()
