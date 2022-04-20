

def main():
    n = int(input())
    t = input()
    s = t[:]
    for d in range(n, 0, -1):
        if n % d == 0:
            s = s[d-1::-1] + s[d:]
    print(s)

if __name__ == "__main__":
    main()