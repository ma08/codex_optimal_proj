
def main():
    n = int(input())
    temperatures = list(map(int, input().split()))
    temperatures.sort()
    for i in range(0, n, 2):
        print(temperatures[i], end=' ')
    for i in range(n - 2, 0, -2):
        print(temperatures[i], end=' ')

if __name__ == '__main__':
    main()
