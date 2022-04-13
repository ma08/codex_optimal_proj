

def main():
    k = int(input())
    d = sorted(list(map(int, input().split())))
    print(max(d[i] - d[i - 1] for i in range(0, k)))

if __name__ == '__main__':
    main()
