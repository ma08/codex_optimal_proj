

def main():
    n = int(input())
    t = input()
    s = t[:]
    for i in range(n, 0, -1):
        if n%i == 0:
            s = s[:i-1:-1] + s[i:]
    print(s)

if __name__ == "__main__":
    main()