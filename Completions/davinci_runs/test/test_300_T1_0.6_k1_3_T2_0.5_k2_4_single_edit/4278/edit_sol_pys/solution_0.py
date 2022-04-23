
def main():
    N = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    a.reverse()
    print(a)

if __name__ == '__main__':
    main()
