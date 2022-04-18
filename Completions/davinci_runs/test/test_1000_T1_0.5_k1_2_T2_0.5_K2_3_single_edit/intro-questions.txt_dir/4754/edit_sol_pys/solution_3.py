

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    arr.reverse()
    print(arr)


if __name__ == "__main__":
    main()
