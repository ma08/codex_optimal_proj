

def main():
    n, a = map(int, input().split())  # n: number of items, a: weight of bag
    e = list(map(int, input().split()))  # e: list of items
    e.sort()  # sort the list
    i = 0
    while a > 0 and i < n:
        if a >= e[i]:  # if the weight of bag is greater than the weight of item
            a -= e[i]
            i += 1
        else:  # if the weight of bag is less than the weight of item
            break
    print(i)  # print number of items

if __name__ == "__main__":
    main()
