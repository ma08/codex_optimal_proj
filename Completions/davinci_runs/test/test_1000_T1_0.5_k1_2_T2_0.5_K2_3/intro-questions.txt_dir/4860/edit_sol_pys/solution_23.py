

def main():
    n = int(input())
    lst = []
    for x in range(n):
        lst.append(int(input()))

    for x in range(1, lst[n-1]+1):
        if x not in lst:
            print(x)


main()
