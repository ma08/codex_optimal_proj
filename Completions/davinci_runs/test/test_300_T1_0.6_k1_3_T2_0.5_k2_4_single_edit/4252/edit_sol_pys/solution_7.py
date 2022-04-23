


def main():
    n = int(input())
    s = input()
    # if n < 3:
    #     print(0)
    #     return
    # if n == 3 and s == 'xxx':
    #     print(3)
    #     return
    count = 0
    for i in range(2, n):
        if s[i - 2] == 'x' and s[i - 1] == 'x' and s[i] == 'x':
            count += 1
    print(count)


if __name__ == '__main__':
    main()
