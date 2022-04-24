

def main():
    q = int(input())
    for _ in range(q):
        n, a, b = map(int, input().split())
        print(n*a)

if __name__ == '__main__':
    main()
