


def main():
    L, R = map(int, input().split())
    min_value = 2018
    for i in range(L, R):
        for j in range(i+1, R+1):
            min_value = min(min_value, (i * j) % 2019)
    print(min_value)


if __name__ == '__main__':
    main()