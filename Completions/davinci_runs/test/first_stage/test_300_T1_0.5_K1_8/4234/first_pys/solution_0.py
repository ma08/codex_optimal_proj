

def main():
    n = int(input())
    s = input()
    k = 0
    for i in range(0, n - 1, 2):
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 1:]
            k += 1
    print(k)
    print(s)

if __name__ == "__main__":
    main()