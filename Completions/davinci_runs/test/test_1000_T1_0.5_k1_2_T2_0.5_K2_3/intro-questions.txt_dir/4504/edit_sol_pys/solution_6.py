

def main():
    s = input()
    # 文字列の最後から逆に走査していく
    n = len(s)
    for i in range(n//2, 0, -1):   # 
        if s[n-i-1:n] == s[n-i*2-1:n-i]:
            print(n-i)
            break

if __name__ == '__main__':
    main()
