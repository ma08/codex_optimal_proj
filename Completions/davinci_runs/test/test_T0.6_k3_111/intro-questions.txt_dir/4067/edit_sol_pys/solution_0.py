
def main():
    n = int(input())
    s = input()

    if n % 3 == 1:
        s = '2' + s

    if n % 3 == 2:
        s = '1' + s

    count_0, count_1, count_2 = 0, 0, 0
    for i in range(n):
        if s[i] == '0':
            count_0 += 1
        elif s[i] == '1':
            count_1 += 1
        else:
            count_2 += 1

    if count_0 == count_1 == count_2:
        print(s)
        return

    # if it's not equal then we need to change something.
    # let's try to change one 0 to 1.
    if count_0 > count_1:
        print('0' * n)
        return

    if count_1 > count_2:
        print('1' * n)
        return

    print('2' * n)

if __name__ == '__main__':
    main()
