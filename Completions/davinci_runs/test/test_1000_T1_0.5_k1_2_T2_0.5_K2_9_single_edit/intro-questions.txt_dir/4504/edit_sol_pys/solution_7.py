

def main():
    s = input()
    n = len(s)
    for i in range(n//2, 0, -1):  # n//2:最長の部分文字列は最長でn/2
        if s[n-i-1:n] == s[n-i*2-1:n-i]:
            print(n-i)
            break

if __name__ == '__main__':
    main()
