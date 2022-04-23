
def main():
    N, Q = map(int, input().split())
    s = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    for i in range(Q):
        ans.append(s[LR[i][0]-1:LR[i][1]].count("AC"))
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
