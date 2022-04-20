

def main(num):
    if num % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif num % 10 in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")

if __name__ == '__main__':
    main(int(input()))