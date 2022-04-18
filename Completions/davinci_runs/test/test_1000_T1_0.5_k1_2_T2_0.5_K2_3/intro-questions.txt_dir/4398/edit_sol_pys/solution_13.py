def main():
    n = int(input())
    s = input()
    t = input()
    res = ''
    for i in range(n):
        res += s[i]
        res += t[i]
    print(res)

if __name__ == '__main__':
    main()
