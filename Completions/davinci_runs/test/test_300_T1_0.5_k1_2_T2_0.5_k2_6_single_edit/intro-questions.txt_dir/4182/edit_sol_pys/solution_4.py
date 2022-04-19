
import sys

def main():
    N, M, X, Y = map(int, input().split())
    x_list = list(map(int, input().split())) + [X]
    y_list = [Y] + list(map(int, input().split()))

    for z in range(X + 1, Y):
        if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):
            print("No War")
            sys.exit()

    print("War")

if __name__ == '__main__':
    main()
