

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = 0
    for i in range(3):
        if a[i] > b[i]:
            x += 1
        elif a[i] < b[i]:
            x -= 1
    print(x)

if __name__ == '__main__':
    main()
