

def main():
    """
    Safe order
    """
    n = int(input()) # number of students
    s = list(map(int, input().split())) # list of students
    s.sort()
    print(s)


if __name__ == '__main__':
    main()
