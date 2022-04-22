

def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    print(sum(a) - max(a) // 2)

if __name__ == '__main__':
    main()
