

def main():
    n = int(input())
    if n == 1:
        print(1)
        return 0
    n = n - 1
    count = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            count = count * 2 + 1
        else:
            count = count * 2 - 1
    print(count)

if __name__ == '__main__':
    main()
