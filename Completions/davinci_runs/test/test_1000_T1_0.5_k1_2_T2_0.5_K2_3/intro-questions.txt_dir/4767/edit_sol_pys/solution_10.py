

def main():
    v2, v3, v5, v7, v11, v13, v17, v19 = [int(i) for i in input().split()]  # read input
    # for i in range(2, 20):
    #    print(i, v2 % i, v3 % i, v5 % i, v7 % i, v11 % i, v13 % i, v17 % i, v19 % i)  # debug
    print(min(20 - v2, 20 - v3, 20 - v5, 20 - v7, 20 - v11, 20 - v13, 20 - v17, 20 - v19))  # output


main()
