
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(enumerate(a, 1))
    a = sorted(a, key=lambda x: x[1])
    for i in a:
        print(i[0])


if __name__ == '__main__':
    main()
