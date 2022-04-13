

def main():
    v2, v3, v5, v7, v11, v13, v17, v19 = map(int, input().split())
    # for i in range(2, 20):
    #     print(i, v2 % i, v3 % i, v5 % i, v7 % i, v11 % i, v13 % i, v17 % i, v19 % i)
    print(min(20 - v2, 6 - v3, 4 - v5, 3 - v7, 2 - v11, 2 - v13, 2 - v17, 2 - v19))


if __name__ == '__main__':
    main()
