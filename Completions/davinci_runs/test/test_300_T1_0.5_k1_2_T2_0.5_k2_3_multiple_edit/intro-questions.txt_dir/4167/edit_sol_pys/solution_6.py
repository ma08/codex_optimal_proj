


import sys

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort()
    ans = arr[0]

    for i in range(1, n):
        ans = (ans + arr[i])/2



    print(ans)

if __name__ == '__main__':
    main()
