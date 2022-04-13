

def main():
    n, k = map(int, input().split())
    s = input()
    k = set(input().split())
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if set(s[i:j]) <= k:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
