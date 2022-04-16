


def main():
    print('Hello world')


if __name__ == '__main__':
    main()


a, b = map(int, input().split())

print(sum(1 for i in range(1, a + 1) if i == int(str(i)[-1])))
