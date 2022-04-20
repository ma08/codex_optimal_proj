

    n = int(input())
    a, b = map(int, input().split())
    k = int(input())
    p = list(map(int, input().split()))
    p.append(a)
    p.append(b)
    if len(set(p)) == n+2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()


def main():
def main():
    x = int(input())
    print(x//500*1000 + (x%500)//5*5)

if __name__ == '__main__':
    main()
