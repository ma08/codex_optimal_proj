

if __name__ == "__main__":
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]
    doublets = 0
    for i in range(N):
        if d[i][0] == d[i][1]:
            doublets += 1
        else:
            doublets = 0
        if doublets == 3:
            print('Yes')
            exit()
    print('No')