import sys

def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline()
    if n == 1:
        print("YES")
        print(0)
    else:
        if s[0] == s[n - 1].strip():
            print("NO")
        else:
            print("YES")
            print(1, end="")
            for i in range(n - 2):
                if (s[i] == s[i + 1].strip() and s[i] == s[n - 1].strip()) or (s[i] == s[i + 1].strip() and s[i] == s[0].strip()):
                    print(0, end="")
                else:
                    print(1, end="")
            print(0)

if __name__ == "__main__":
    main()
