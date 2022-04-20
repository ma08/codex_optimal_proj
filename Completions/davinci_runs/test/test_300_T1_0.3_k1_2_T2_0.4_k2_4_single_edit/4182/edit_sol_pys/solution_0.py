

def main():
    n, m, x, y = map(int, input().split())
    x_list = map(int, input().split())
    y_list = map(int, input().split())

    if x < y:
        if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):
            print("No War")
        else:
            print("War")
    else:
        print("War")

if __name__ == '__main__':
    main()
