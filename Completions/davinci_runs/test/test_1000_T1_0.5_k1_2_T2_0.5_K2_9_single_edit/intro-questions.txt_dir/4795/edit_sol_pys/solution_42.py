
def main():
    n = int(input())
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        print(a + b)

if __name__ == '__main__':
    main()
