
def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        if a == 1:
            print(0)
        else:
            print(max(2 * b - a, a - 2 * b))

if __name__ == '__main__':
    main()
