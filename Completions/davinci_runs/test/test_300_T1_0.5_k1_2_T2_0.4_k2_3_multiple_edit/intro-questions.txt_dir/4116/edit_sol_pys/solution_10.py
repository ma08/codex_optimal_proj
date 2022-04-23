

N = int(input())


def divisible_by_2_and_5(number):
    if number % 2 == 0 and number % 5 == 0:
        print('Yes')
    elif number % 3 == 0 and number % 5 == 0:
        print('Yes')
    elif number % 2 == 0 and number % 3 == 0:
        print('Yes')
    else:
        print('No')


divisible_by_2_and_5(N)
