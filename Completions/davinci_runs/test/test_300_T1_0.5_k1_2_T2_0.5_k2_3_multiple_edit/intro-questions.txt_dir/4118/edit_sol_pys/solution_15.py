
def main():
    a, b = map(int, input().split())
    for i in range(1,10):
        for j in range(1,10):
            if a == i*j:
                a = i
                b = j
    print(a*b)


if __name__ == '__main__':
    main()
