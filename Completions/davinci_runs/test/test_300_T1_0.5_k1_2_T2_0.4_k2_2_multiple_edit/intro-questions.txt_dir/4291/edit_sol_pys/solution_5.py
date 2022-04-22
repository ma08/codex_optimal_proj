

def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]  # リスト内包表記
    ans = []
    for i in range(q):
        ans.append(s[lr[i][0]-1:lr[i][1]].count("AC"))  # リスト内包表記
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
