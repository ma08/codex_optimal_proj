

def main():
    n,k = map(int,input().split())
    s = list(input())
    count = 0
    # print(s)
    while len(s) > 0:
        print(s)
        if len(s) >= 2:
            if s[0] == s[1]:
                # print(s[0])
                count += 1
                s = s[1:]
            else:
                count += n - 1
                s = s[1:]
        else:
            count += n - 1
            s = s[1:]
    print(count)

if __name__ == "__main__":
    main()