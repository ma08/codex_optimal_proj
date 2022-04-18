


def main():
    k = int(input())
    if k == 1:
        print(1, 0)
        return
    b = 1
    breaks = 0
    while b < k:
        b *= 2
        breaks += 1
    print(b, breaks)

if __name__ == '__main__':
    main()
