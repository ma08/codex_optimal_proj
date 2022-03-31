
def main():
    n = int(input())
    a = list(map(int, input().split()))[::-1]
    for i in range(n):
        if a[i] > i + 1:
            print("NO")
            exit()
    print("YES")    


if __name__ == '__main__':
    main()
