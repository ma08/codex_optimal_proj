

def main():
    n = int(input())
    l = [input() for _ in range(n)]
    s = set(l)
    print(len(s))

if __name__ == "__main__":
    main()
