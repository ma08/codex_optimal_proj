

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                print(i, j)

if __name__ == '__main__':
    main()
