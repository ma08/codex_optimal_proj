

def main():
    n = int(input())  # number of students
    a = [int(x) for x in input().split()]  # list of arrival times
    b = [int(x) for x in input().split()]  # list of departure times
    c = [(x + y) % n for (x, y) in zip(a, b)]  # list of students
    c.sort()  # sort the list
    print(' '.join([str(x) for x in c]))  # print the sorted list

if __name__ == '__main__':
    main()
