if __name__ == '__main__':
    n = int(input())
    if n % 2 == 0:
        if n >= 2 and n <= 5:  # 2, 3, 4, 5
            print("Not Weird")
        elif n >= 6 and n <= 20:  # 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
            print("Weird")
        else:
            print("Not Weird")
