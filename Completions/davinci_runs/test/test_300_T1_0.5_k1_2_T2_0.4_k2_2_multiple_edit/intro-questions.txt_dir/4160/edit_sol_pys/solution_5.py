

def main():
    x = input()
    count = 0
    balance = 0
    for i in x:
        count += 1
        if i == "A":
            balance += 4
        elif i == "B":
            balance += 3
        elif i == "C":
            balance += 2
        elif i == "D":
            balance += 1
    print(count)

if __name__ == '__main__':
    main()
