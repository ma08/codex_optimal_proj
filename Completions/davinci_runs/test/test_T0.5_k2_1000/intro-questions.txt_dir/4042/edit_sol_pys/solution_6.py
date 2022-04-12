

def main():
    x = float(input())  # number for search

    for i in range(1, 10):  # iterate all numbers from 1 to 9
        for j in range(1, 10):  # iterate all numbers from 1 to 9
            if i / j == x:  # if division corresponds to the number for search
                print(i, j)  # print numbers
                break

if __name__ == '__main__':
    main()
