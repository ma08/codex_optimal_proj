

def main():
    N, M = map(int, input().split())  # N:人数, M:友達関係
    A = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append([a, b])  # 友達関係をリストに格納
    print(A)

if __name__ == "__main__":
    main()
