

def main():
    n = int(input())  # n = 3
    d = [int(x) for x in input().split()]  # d = [1, 2, 3]
    d.sort()
    print(d[-1] - d[0])

if __name__ == "__main__":
    main()
