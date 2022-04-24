
def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort()
    count = 0
    for i in range(n):
        count += a[i] - 1
    print(count)




if __name__ == '__main__':
    main()
