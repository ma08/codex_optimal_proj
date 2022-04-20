

def main():
    N, M = map(int, input().split())
    A = set()
    for i in range(M):
        a, b = map(int, input().split())
        A.add((a, b))
    print(A)

if __name__ == "__main__":
    main()
