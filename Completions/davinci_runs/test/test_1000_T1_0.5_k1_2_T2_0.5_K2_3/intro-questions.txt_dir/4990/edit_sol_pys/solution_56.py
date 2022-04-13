import math

def main():
    b, g = [int(x) for x in input().split()]  # b - number of books, g - number of groups
    print(math.ceil(b/g))  # number of groups

if __name__ == "__main__":
    main()
