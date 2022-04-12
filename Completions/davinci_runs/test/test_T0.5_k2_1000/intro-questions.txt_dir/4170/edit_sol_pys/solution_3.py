
def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    print(sum(a) - sum(b))

if __name__ == '__main__':
    main()
