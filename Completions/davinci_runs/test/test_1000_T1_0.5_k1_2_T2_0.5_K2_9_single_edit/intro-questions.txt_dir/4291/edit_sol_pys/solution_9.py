

def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for i in range(q)]
    ans = []
    for j in range(q):
        ans.append(s[lr[j][0]-1:lr[j][1]].count("AC"))
    for j in ans:
        print(j)

if __name__ == '__main__':
    main()
