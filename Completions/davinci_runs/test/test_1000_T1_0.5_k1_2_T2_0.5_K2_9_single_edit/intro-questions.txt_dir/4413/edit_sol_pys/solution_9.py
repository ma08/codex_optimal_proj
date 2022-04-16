

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))[1:]
        print(len(set(a)) - 1)


if __name__ == '__main__':
    main()
