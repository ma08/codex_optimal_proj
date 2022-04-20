


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = list(enumerate(a, 1))  # enumerate adds index to each element
    a = sorted(a, key=lambda x: x[1])  # sort by second element
    a = [i[0] for i in a]  # get first elements
    print(*a, sep='\n')


if __name__ == '__main__':
    main()
