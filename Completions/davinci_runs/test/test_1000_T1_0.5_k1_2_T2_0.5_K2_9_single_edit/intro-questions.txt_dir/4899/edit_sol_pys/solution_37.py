

def main():
    n = int(input())
    s = input().split()
    for i in range(n):
        s[i] = int(s[i])
    print(sum(s))

if __name__ == '__main__':
    main()
