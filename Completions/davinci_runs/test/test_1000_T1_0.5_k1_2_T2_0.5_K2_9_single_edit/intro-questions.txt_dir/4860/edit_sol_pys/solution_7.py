

def main():
    n = int(input())
    l = []
    for x in range(n):
        l.append(int(input()))

    for x in range(1,l[n-1]+1):
        if x not in l:
            print(x)


main()
