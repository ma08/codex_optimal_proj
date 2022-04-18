

def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]  # lr[i][0] = l, lr[i][1] = r
    ans = [0] * q
    for i in range(q):
        ans[i] = s[lr[i][0]-1:lr[i][1]].count("AC")
    for i in range(q):
        print(ans[i])

if __name__ == '__main__':
    main()
