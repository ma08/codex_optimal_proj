

def main():
    a, b, c, d, e, f = map(int, input().split())
    print(max(c, f) - min(a, d), max(e, b) - min(b, e))

if __name__ == '__main__':
    main()
