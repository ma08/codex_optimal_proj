def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]
    ans = []
    for i in lr:
        ans.append(s[i[0]-1:i[1]].count("AC"))
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
