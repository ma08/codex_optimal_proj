

def main():
    n, m = map(int, input().split())
    s = list(input())
    t = list(input())

    for i in range(n):
        if t[i] == s[i]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
