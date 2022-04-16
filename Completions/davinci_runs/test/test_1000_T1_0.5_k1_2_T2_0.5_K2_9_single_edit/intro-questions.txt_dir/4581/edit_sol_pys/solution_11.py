# coding: utf-8



def main():
    s = input()
    price = 700
    for char in s:
        if char == 'o':
            price += 100
    print(price)


if __name__ == '__main__':
    main()
