

def main():
    a, b = map(int, input().split())
    m = [2, 3, 5, 7]
    if (a in m and b in m) or a == 1 or b == 1:
        print(a * b)
    else:
        print(-1)

if __name__ == '__main__':
    main()
