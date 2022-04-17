

def check(arr):
    if arr[0] == arr[-1]:
        return 0
    else:
        return 2

def main():
    for _ in range(int(input())):
        n = int(input())
        b = [int(x) for x in input().split()]
        if n == 1:
            print(0)
        elif n == 2:
            print(0)
        else:
            d = [b[i] - b[i - 1] for i in range(1, n)]
            d.sort()
            print(check(d))

if __name__ == '__main__':
    main()
