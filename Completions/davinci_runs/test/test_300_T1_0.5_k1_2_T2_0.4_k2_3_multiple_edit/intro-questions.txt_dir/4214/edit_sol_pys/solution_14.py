

def main():
    n = int(input())
    d = [int(i) for i in input().split()]
    d.sort()
    print(d[n//2] - d[n//2 - 1])

if __name__ == "__main__":
    main()
