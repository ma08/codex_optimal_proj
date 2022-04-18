

def main():
    n = int(input())  # number of people
    a = int(input())  # number of people who can eat a
    b = int(input())  # number of people who can eat b
    c = int(input())  # number of people who can eat c
    d = int(input())  # number of people who can eat d
    e = int(input())  # number of people who can eat e

    l = [a, b, c, d, e]  # list of people who can eat
    l.sort()  # sort the list

    if n <= l[0]:
        print(1)  # if all people can eat one of the meals
    else:
        print(2)  # if not all people can eat one of the meals

if __name__ == '__main__':
    main()
