

def main():
    n, d, k = map(int, input().split())
    for i in range(d):
        for j in range(k):
            print(i + 1, i + 2)
        print(1, i + 2)

if __name__ == '__main__':
    main()
