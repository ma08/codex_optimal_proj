#coding:utf-8

def main():
    N,M,X = map(int,input().split())
    CA = [list(map(int,input().split())) for _ in range(N)]
    ans = float('inf')
    for bit in range(1<<N):
        cost = 0
        skill = [0]*M
        for i in range(N):
            if bit & (1<<i):
                cost += CA[i][0]
                for j in range(M):
                    skill[j] += CA[i][j+1]
        if min(skill) >= X:
            ans = min(ans,cost)
    if ans == float('inf'):
        ans = -1
    print(ans)
if __name__ == '__main__':
    main()
