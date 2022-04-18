

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum([abs(i-sum(a)/n)**2 for i in a])/n)


if __name__ == '__main__':
    main()
