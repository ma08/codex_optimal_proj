

def main():
    a, b = map(int, input().split())
    if a == 2 or a == 3 or a == 5 or a == 7:
        if b == 2 or b == 3 or b == 5 or b == 7:
            print(a * b) return
    elif a == 4 or a == 6 or a == 8:
        if b == 4 or b == 6 or b == 8:
            print(a * b) return
    elif a == 9:
        if b == 9:
            print(a * b) return
    else:
        print(-1)

if __name__ == '__main__':
    main()
