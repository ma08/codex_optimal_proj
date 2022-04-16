
def main():
    n, a = [int(x) for x in input().split()]  # n = number of elements in array, a = element to be searched
    e = [int(x) for x in input().split()]  # e = array
    e.sort()
    i = 0
    while a > 0 and i < n:
        if e[i] < a:
            a -= e[i]
            i += 1
        else:
            break
    print(i)  # number of elements to be removed

if __name__ == "__main__":
    main()
