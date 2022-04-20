
def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    print(l[-1] - l[0])

if __name__ == '__main__':
    main()
