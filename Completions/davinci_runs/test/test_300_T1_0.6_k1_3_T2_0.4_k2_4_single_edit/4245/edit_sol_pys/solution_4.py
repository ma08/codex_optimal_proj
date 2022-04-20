
def main():
    a, b = map(int, input().split())
    count = 0
    while b > 0:
        if b >= a:
            b -= a
        else:
            b -= 1
        count += 1
    print(count)

if __name__ == '__main__':
    main()
