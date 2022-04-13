
def main():
    n = int(input())
    s = list(input())
    t = list(input())
    res = []
    for i in range(2*n):
        if i % 2 == 0:
            res.append(s[i//2])
        else:
            res.append(t[i//2])
    print(res)


if __name__ == '__main__':
    main()
