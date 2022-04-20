

def is_sorted(s):
    for i in range(len(s) - 1):
        if (s[i + 1] < s[i]):
            return False
    return True

def main():
    n = int(input())
    s = input()
    if (is_sorted(s)):
        print(0)
        print(s)
        return 0
    i = 0
    j = 0
    while (i < n):
        while (j < n and s[j] == s[i]):
            j += 1
        i = j
        j = i + 1
        print(i, j)
    return

if __name__ == "__main__":
    main()
