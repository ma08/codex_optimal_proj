
def main():
    n, t = map(int, input().split())
    times = map(int, input().split())
    total = 0
    for i in range(n):
        total += times[i]
        if total > t:
            print(i)
            exit()
    else:
        print(n)

if __name__ == '__main__':
    main()
