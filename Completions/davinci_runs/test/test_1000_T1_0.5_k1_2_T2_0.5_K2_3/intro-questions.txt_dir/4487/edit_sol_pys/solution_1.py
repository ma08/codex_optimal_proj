

def main():
    a, b, c, d = map(str, input().split())
    if a[-1] == b[0] and b[-1] == c[0] and c[-1] == d[0]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
