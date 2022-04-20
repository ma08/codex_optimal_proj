

def main():
    t = int(input())
    for i in range(t):
        n, k = [int(x) for x in input().split()]
        print(n//k + (1 if n%k else 0))

if __name__ == '__main__':
    main()