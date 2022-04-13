import math

def main():
    b, k, g = [int(x) for x in input().split()]  # b - number of books, k - number of students, g - number of groups
    print(math.ceil(b/g))  # number of groups

if __name__ == "__main__":
    main()
