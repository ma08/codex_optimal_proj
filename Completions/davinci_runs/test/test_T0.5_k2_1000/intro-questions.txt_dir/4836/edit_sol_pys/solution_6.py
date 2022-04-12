

def main():
    n, c = map(int, input().split())  # n: number of items, c: capacity
    w = list(map(int, input().split()))  # w: weights
    weights = sorted(w)  # sort weights

    i = 0  # index
    total = 0  # total weight
    while i < n:  # loop through all items
        if total + weights[i] <= c:  # if total weight + current weight <= capacity
            total += weights[i]  # add current weight to total
            i += 1  # increment index
        else:
            break  # else, break

    print(i)  # print number of items

if __name__ == "__main__":
    main()
