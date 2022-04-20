


def solve(a):
    a.sort()
    if len(a) % 2 == 0:
        if a[0] == a[-1]:
            return 0
        else:
            return -1
    else:
        if a[0] == a[-1]:
            return 0
        else:
            if a[0] + 1 == a[-1]:
                return 1
            else:
                return -1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

if __name__ == '__main__':
    main()
