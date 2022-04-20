

def main():
    n, x, y = map(int, input().split())
    s = input()
    s = s[:y] + '1'*(x-y) + s[x:]
    print(s.count('0'))

if __name__ == "__main__":
    main()