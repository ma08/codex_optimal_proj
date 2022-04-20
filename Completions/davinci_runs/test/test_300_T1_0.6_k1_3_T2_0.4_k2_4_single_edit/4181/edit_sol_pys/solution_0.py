

def main(n, a, b, c):
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    for i in range(n):
        pass

    return 0

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(main(n, a, b, c))
