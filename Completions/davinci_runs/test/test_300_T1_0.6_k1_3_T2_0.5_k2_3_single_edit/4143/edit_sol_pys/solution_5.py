

def main():
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    c = int(raw_input())
    d = int(raw_input())
    e = int(raw_input())

    l = [a, b, c, d, e]
    l.sort()

    if n <= l[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
