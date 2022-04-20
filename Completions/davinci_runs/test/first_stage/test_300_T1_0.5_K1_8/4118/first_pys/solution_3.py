

def main():
    a, b = map(int, input().split())
    if a in [2, 3, 5, 7] and b in [2, 3, 5, 7]:
        print(a * b)
    else:
        print(-1)

if __name__ == '__main__':
    main()