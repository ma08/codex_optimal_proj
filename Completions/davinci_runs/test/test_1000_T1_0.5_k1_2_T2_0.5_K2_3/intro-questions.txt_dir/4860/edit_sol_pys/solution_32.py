

def main():
    n = int(input())  # number of test cases

    for x in range(n):
        m = int(input())  # number of integers
        list = []
        for y in range(m):
            list.append(int(input()))

        for y in range(1, list[m - 1] + 1):
            if y not in list:
                print(y)


main()
