

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = set(map(int, input().split()))
        print(len(a))


if __name__ == '__main__':
    main()
