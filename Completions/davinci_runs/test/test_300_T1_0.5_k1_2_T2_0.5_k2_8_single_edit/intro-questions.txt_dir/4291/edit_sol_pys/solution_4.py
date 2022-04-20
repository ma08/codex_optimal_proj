

def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]
    for i, j in lr:
        print(s[i-1:j].count("AC"))

if __name__ == '__main__':
    main()
