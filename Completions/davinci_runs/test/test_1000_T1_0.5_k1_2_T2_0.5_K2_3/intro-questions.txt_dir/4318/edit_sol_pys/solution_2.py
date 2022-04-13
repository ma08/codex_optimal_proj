
def main():
    n = int(input())  # number of elements
    h = list(map(int, input().split()))  # list of height
    h.sort(reverse=True)  # sort in descending order
    print(h.index(h[0]) + 1)  # print the index of the tallest person 


if __name__ == '__main__':
    main()
