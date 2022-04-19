

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    for z in range(x+1, y+1):
        if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):
            print("No War")
            return
    print("War")

if __name__ == '__main__':
    main()
