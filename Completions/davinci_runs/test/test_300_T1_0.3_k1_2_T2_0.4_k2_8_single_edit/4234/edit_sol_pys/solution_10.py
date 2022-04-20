

def main():
    n = int(input())
    s = input()
    k = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            k += 1
    print(k)
    if k == 0:
        print(s)
    else:
        for i in range(n-1):
            if s[i] == s[i+1]:
                continue
            print(s[i], end="")
        print()

if __name__ == "__main__":
    main()
