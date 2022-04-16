

def main():
    n, a = [int(x) for x in input().split()]
    e = [int(x) for x in input().split()] # list of integers
    e.sort()
    i = 0
    while a > 0 and i < n: # while a is greater than 0 and i is less than n
        if e[i] < a: # if the element at index i is less than a
            a -= e[i]
            i += 1
        else:
            break
    print(i)

if __name__ == "__main__":
    main()
