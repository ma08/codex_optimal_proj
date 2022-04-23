
def main():
    n = int(input())
    b = list(map(int, input().split()))
    b = list(enumerate(b, 1))
    b = sorted(b, key=lambda x: x[1])
    b = [i[0] for i in b]
    print(*b, sep='\n')


if __name__ == '__main__':
    main()
