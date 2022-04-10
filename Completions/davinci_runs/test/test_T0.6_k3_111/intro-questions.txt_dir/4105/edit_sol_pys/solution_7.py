

def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    print(l[-1]-l[0])

if __name__ == '__main__':
    main()
