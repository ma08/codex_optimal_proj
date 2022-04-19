

def main():
    a, b = map(int, input().split())
    if a == b:
        print(0)
        return
    if a > b:
        print(-1)
        return
    count = 0
    while a < b:
        if a * 2 <= b:
            a *= 2
        elif a * 3 <= b:
            a *= 3
        else:
            print(-1)
            return
        count += 1
    print(count)

if __name__ == '__main__':
    main()
