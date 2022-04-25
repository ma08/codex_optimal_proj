
def main():
    n, q = map(int, input().split())
    s = input()
    l_r = [list(map(int, input().split())) for _ in range(q)]
    ans = []
    for i in range(q):
        ans.append(s[l_r[i][0] - 1:l_r[i][1]].count("AC"))
    for i in ans:
        print(i)


if __name__ == '__main__':
    main()
