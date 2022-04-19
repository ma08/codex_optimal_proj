

def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        a[i] = int(input())
    for i in range(n):
        if a[i] % 2 == 0:
            print(a[i] // 2)
        else:
            print(a[i] // 2 + 1)

if __name__ == '__main__':
    main()
