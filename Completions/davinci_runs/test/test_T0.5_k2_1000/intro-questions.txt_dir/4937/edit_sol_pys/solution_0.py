

def main():
    n, a = map(int, input().split())  # n: number of items, a: capacity of bag
    e = list(map(int, input().split()))  # e: list of items (elements)
    e.sort()  # sort list of items
    i = 0  # index
    while a > 0 and i < n:  # while capacity of bag is greater than 0 and index is less than number of items
        if a >= e[i]:  # if capacity of bag is greater than or equal to item
            a -= e[i]  # capacity of bag is decreased by item
            i += 1  # index is increased by 1
        else:  # if capacity of bag is less than item
            break  # break
    print(i)  # print index

if __name__ == "__main__":
    main()
