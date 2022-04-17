
import sys

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split())) + [x]
    y_list = list(map(int, input().split())) + [y]

    if all(x_i < y_i for x_i, y_i in zip(x_list, y_list)):
        print("No War")
        sys.exit()

    print("War")

if __name__ == '__main__':
    main()
