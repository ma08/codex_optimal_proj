

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] > a[-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
