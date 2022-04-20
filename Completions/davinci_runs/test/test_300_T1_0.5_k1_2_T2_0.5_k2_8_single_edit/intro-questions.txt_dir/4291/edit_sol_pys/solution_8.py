

def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)] # lr = [[l, r], [l, r], ...]
    ans = []
    for i in range(q):
        ans.append(s[lr[i][0]-1:lr[i][1]].count("AC"))
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
