

def main():
    n, a = map(int, input().split())  # n is the number of elements and a is the number of elements to add
    e = list(map(int, input().split()))  # e is the list of elements
    e.sort()  # sort the list of elements
    i = 0
    while a > 0 and i < n:
        if a >= e[i]:
            a -= e[i]
            i += 1
        else:
            break
    print(i)


if __name__ == "__main__":
    main()
