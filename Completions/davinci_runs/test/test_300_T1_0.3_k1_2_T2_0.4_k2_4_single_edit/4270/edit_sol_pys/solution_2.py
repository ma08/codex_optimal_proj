def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    while len(v) > 1:
        a = v.pop()
        b = v.pop()
        v.append((a + b) / 2)
        v.sort()
    print(v[0])


if __name__ == '__main__':
    main()
