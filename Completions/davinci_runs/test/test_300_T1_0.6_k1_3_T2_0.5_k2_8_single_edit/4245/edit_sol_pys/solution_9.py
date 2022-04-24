

def main():
    a, b = map(int, input().split())
    count = 0
    if b % a == 0:
        count = b // a
    else:
        count = (b // a) + 1
        count += 1
    print(count)

if __name__ == '__main__':
    main()
