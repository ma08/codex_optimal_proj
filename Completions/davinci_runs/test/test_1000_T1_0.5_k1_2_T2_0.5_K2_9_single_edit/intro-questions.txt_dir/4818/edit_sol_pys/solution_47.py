

def main():
    n = int(input())
    lst = list(map(int, input().split()))

    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in d:
        if d[i] == 1:
            print(i)
            break
    else:
        print("None")

if __name__ == '__main__':
    main()
