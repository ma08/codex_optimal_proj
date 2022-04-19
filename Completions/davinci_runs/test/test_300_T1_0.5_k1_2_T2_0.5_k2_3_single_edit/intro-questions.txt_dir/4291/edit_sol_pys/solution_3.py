

def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]
    ans = [s[lr[i][0]-1:lr[i][1]].count("AC") for i in range(q)]
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
