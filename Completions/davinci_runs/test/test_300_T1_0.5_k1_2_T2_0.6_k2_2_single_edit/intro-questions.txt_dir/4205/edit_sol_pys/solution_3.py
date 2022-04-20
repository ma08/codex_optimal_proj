def main():
    n = int(input())
    sequence = list(map(int, input().split()))


    if sequence == sorted(sequence):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
