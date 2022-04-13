def main():
    n = int(input())
    s = input()
    t = input()
    result = ''
    for i in range(n):
        result += s[i]
        result += t[i]
    print(result)

if __name__ == '__main__':
    main()
