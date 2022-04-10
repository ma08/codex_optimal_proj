

def main():
    x = float(input())
    for i in range(1,11):
        for j in range(1,11):
            if abs(x - i/j) < 0.000001:
                print(i, j)
                return

if __name__ == '__main__':
    main()