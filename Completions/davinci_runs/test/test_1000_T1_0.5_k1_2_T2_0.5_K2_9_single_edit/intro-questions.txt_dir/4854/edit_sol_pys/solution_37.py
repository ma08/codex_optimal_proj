
def main():
    n, c = map(int, input().split())
    a = [0] * c
    for i in map(int, input().split()):
        a[i - 1] += 1
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()
