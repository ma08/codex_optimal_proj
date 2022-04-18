

def main():
    a, b, c = input().split()
    if a[-1] == b[0] and b[-1] == c[0] and a[0] == c[-1]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
