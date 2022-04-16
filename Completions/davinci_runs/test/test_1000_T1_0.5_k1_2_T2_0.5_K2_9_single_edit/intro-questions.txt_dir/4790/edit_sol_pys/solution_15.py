
def main():
    stones = input().strip()
    balance = 0
    for i in range(len(stones)):
        if stones[i] == 'B':
            balance += i+1
        else:
            balance -= i+1
    if balance == 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
