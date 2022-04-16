

def main():
    stones = input().upper()
    balance = 0
    for stone in stones:
        if stone == 'W':
            balance += 1
        else:
            balance -= 1
    if balance == 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
