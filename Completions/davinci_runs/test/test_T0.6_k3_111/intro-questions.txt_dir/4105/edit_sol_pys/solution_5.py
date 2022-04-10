

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    print(arr[n//2])

if __name__ == '__main__':
    main()
