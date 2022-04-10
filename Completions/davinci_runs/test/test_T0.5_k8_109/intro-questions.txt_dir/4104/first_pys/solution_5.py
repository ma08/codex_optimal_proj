

def main():
    s = input()

    res = s.split('+')
    res = [int(x) for x in res]
    res = sum(res)

    res = s.split('-')
    res = [int(x) for x in res]
    res = sum(res)

    print(res)


if __name__ == '__main__':
    main()