

def main():
    n = int(input())
    s = input()
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = i
    print(d)

if __name__ == '__main__':
    main()
