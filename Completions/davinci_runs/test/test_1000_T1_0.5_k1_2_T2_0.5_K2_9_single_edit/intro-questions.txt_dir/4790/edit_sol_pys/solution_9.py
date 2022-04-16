import math

def main():
    stones = input()
    balance = 0
    for stone in stones:
        if stone == 'B':
            balance += 1
        else:
            balance -= 1
    if balance == 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
