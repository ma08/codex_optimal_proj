

def main():
    stones = input().strip()
    balance = 0
    for stone in stones:
        if stone == 'B':
            balance += 1
        else:
            balance -= 1
    print(1 if balance == 0 else 0)

if __name__ == "__main__":
    main()
