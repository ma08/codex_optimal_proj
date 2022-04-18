
import sys

def main():
    n, m, x, y = map(int, input().split())
    x_list = [int(i) for i in input().split()]
    y_list = [int(i) for i in input().split()]

    for z in range(x + 1, y):
        if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):
            print("No War")
            exit()

    print("War")

if __name__ == '__main__':
    main()
