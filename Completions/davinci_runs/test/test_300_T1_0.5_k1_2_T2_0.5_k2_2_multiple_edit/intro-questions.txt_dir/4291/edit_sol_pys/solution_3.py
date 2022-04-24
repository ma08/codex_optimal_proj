
def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]
    for i in lr:
        print(s[i[0]-1:i[1]].count("AC"))

if __name__ == '__main__':
    main()
