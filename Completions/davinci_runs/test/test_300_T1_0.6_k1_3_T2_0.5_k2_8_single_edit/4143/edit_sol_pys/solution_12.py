

def main():
    n = int(input())
    l = []
    for i in range(5):
        l.append(int(input()))

    l.sort()

    if n <= l[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
