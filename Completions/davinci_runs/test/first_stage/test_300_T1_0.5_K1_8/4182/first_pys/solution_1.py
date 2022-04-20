

def main():
    n, m, x, y = map(int, input().split())
    x_s = set(map(int, input().split()))
    y_s = set(map(int, input().split()))
    if x<y:
        for i in range(x+1, y):
            if i not in x_s and i in y_s:
                print("No War")
                exit()
    print("War")

if __name__ == '__main__':
    main()