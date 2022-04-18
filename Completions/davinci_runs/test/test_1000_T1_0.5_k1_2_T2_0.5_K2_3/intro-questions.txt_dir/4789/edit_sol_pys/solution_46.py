

def main():
    k = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(max(d[i] - d[i - 1] for i in range(1, len(d))))

if __name__ == '__main__':
    main()
