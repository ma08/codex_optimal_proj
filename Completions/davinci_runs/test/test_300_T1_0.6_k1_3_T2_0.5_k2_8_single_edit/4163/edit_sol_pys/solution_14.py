

import math

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def main():
    n = int(input())
    doublets = []

    for i in range(n):
        dice1, dice2 = map(int, input().split())
        doublets.append(dice1 == dice2)

    for i in range(len(doublets) - 2):
        if doublets[i] and doublets[i+1] and doublets[i+2]:
            print("Yes")
            exit()

    print("No")

if __name__ == '__main__':
    main()
