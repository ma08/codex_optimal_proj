
def main():
    k = int(input())
    a = 0
    b = 1
    for i in range(k - 1):
        a, b = b, a + b
    print(a, b)


if __name__ == '__main__':
    main()
