
def main():
    x = int(input())
    genders = input()

    women = 0
    men = 0
    total = 0

    for gender in genders:
        if gender == 'W':
            women += 1
        else:
            men += 1
        if abs(men - women) <= x:
            total += 1
        else:
            break

    print(total)

if __name__ == '__main__':
    main()
