

def main():
    N, M = map(int, input().split())  # N: number of people, M: number of pairs
    A = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append([a, b])  # a, b: a pair of people
    print(A)  # A: a list of pairs

if __name__ == "__main__":
    main()
