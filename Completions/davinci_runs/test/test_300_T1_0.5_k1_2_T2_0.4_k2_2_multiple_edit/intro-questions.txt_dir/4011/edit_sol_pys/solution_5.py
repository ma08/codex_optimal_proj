

def main():
    n = int(input())
    s = list(input())
    t = list(map(int, input().split())) + [0]

    for i in range(n):
        s[i] = t[int(s[i])]

    s = ''.join(s)

    print(s)

if __name__ == '__main__':
    main()
