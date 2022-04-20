

def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()

    while len(s) > 1:
        s[0] = (s[0] + s[1]) / 2
        s.pop(1)
        s.sort()

    print(s[0])

if __name__ == '__main__':
    main()
