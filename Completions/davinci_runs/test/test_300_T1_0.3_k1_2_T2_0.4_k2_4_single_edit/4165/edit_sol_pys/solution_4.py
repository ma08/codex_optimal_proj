

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    abc = a + b + c
    abc.sort()
    print(abc)

if __name__ == '__main__':
    main()
