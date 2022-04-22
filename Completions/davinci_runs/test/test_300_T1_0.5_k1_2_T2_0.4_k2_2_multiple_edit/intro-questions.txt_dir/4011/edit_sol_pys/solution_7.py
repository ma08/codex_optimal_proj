

def main():
    n = int(input())
    s = list(input())
    t = list(map(str, input().split()))
    t = [0] + t

    for i in range(n):
        s[i] = t[int(s[i])-1]

    s = ''.join(s)

    print(s)

if __name__ == '__main__':
    main()
