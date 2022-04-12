

def main():
    v2, v3, v5, v7, v11, v13, v17, v19 = [int(i) for i in input().split()] # read input
    print(min(20 - v2, 6 - v3, 4 - v5, 3 - v7, 2 - v11, 2 - v13, 2 - v17, 2 - v19)) # print answer

main()
