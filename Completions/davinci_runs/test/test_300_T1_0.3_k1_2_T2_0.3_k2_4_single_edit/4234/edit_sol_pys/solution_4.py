

def main():
    n = int(input())
    s = input().strip()
    k = 0
    for i in range(0, n, 2):
        if i+1 < n and s[i] == s[i+1]:
            k += 1
    print(k, end="\n")
    if k == 0:
        print(s, end="\n")
    else:
        for i in range(0, n, 2):
            if i+1 < n and s[i] == s[i+1]:
                continue
            print(s[i], end="\n")

if __name__ == "__main__":
    main()
