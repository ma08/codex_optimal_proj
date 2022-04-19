
def main():
    a = int(input())  # input an integer
    while True:
        if a % 4 == 0:  # check if the number is divisible by 4
            print(a)
            break  # break the loop
        else:
            a += 1

if __name__ == '__main__':
    main()
