

def main():
    n, m = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(m)]
    ans = []
    for i in range(q):
        ans.append(s[lr[i][0]-1:lr[i][1]].count("AC"))
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
