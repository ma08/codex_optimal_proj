
def main():
    x = float(input())

    for i in range(1, 10):  # 1 to 9
        for j in range(1, 10):  # 1 to 9
            if i / j == x:
                print(i, j)  # print i and j
                break  # break out of the loop

if __name__ == '__main__':
    main()
