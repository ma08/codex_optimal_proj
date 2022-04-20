
import sys

def main():
    n, x = map(int, input().split())
    x_lst = [int(i) for i in input().split()]
    x_lst.sort()  # sort the list

    if x in x_lst:  # if x is in the list, remove it
        x_lst.remove(x)  # remove x from the list

    min_d = max(x_lst[0] - x, x - x_lst[-1])  # calculate the distance between x and the closest number
    for i in range(1, n):
        min_d = max(min_d, (x_lst[i] - x_lst[i - 1]) // 2)  # calculate the distance between the closest numbers

    print(min_d)

if __name__ == '__main__':
    main()
