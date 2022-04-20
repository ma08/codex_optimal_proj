

def main():
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    #print(a)
    max_value = a[k-1]
    min_value = a[k]
    if k == 0:
        print(1)
    elif k == n:
        print(a[k-1])
    else:
        if max_value == min_value:
            print(-1)
        else:
            print(max_value)


if __name__ == "__main__":
    main()