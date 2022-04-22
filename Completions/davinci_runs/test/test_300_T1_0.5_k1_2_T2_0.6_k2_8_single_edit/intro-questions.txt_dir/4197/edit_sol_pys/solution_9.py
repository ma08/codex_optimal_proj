



def main():
    n = int(input())
    # this is a generator
    a = list(map(int, input().split()))
    a = list(enumerate(a, 1))
    a = sorted(a, key=lambda x: x[1])
    a = [i[0] for i in a]  # list comprehension
    print(*a, sep='\n')


if __name__ == '__main__':
    main()
