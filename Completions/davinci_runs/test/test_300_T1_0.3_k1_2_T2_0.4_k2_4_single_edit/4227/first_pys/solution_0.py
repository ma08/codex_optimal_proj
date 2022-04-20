

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append([a, b])
    print(A)

if __name__ == "__main__":
    main()