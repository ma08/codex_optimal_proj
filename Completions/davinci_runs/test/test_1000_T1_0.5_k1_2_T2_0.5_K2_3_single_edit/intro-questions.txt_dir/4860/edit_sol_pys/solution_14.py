

def main():
    n = int(input())
    list = []
    for x in range(n):
        list.append(int(input()))

    for x in range(1, list[n-1]+1):
        if x not in list:
            print(x)


main()
