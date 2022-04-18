

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        print(a, b)

if __name__ == "__main__":
    main()
