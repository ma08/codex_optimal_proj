

def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]
    ans = []
    for i in range(q):
        ans.append(s[lr[i][0]-1:lr[i][1]].count("AC"))  # s[l-1:r].count("AC")
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
