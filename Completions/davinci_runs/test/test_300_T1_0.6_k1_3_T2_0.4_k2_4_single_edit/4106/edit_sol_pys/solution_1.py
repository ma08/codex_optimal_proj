def main():
    s = input()
    n = int(input())
    for _ in range(n):
        a, b = map(int,input().split())
        tmp = s[a-1:b]
        s = s[:a-1] + tmp[::-1] + s[b:]
    print(s)



if __name__ == '__main__':
    main()
