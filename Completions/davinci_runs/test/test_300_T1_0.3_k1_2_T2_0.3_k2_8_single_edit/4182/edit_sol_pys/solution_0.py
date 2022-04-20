

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    if x < y:
        for z in range(x+1, y+1):  # x+1 <= z <= y
            if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):  # z > x_i and z <= y_i
                print("No War")
                return
        print("War")
    else:
        print("War")

if __name__ == '__main__':
    main()
