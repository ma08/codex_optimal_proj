# https://atcoder.jp/contests/abc087/tasks/arc090_a

def main():
    n, q = map(int, input().split())
    s = list(input())
    lr = [list(map(int, input().split())) for _ in range(q)]
    ans = []
    for i in range(q):
        ans.append(s[lr[i][0]-1:lr[i][1]].count("AC"))  # listのスライスは、[start:end]
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
