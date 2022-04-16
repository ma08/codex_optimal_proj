

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[n//2])

main()
