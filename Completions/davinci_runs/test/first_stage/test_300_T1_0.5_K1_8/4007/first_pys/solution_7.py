

def main():
    n = int(input())
    f = list(map(int, input().split()))
    f = [0 if x == 0 else x for x in f]
    f = [x if x != 0 else n+1 for x in f]
    f = [x if x != 0 else n+2 for x in f]
    f = [x if x != 0 else n+3 for x in f]
    f = [x if x != 0 else n+4 for x in f]
    f = [x if x != 0 else n+5 for x in f]
    f = [x if x != 0 else n+6 for x in f]
    f = [x if x != 0 else n+7 for x in f]
    f = [x if x != 0 else n+8 for x in f]
    print(*f)

if __name__ == '__main__':
    main()