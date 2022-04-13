

def main():
    shares = []
    for i in range(int(input())):  # iterate through the number of commands
        temp = input().split()  # split the command
        if temp[0] == "buy":
            shares.append(int(temp[1]) * int(temp[2]))  # buy a share at a price
        elif temp[0] == "sell":
            shares.sort()  # sort the shares
            for j in range(int(temp[1])):  # sell the amount of shares in the command
                shares[j] = int(temp[2]) - shares[j]  # subtract the share price from the sale price
        elif temp[0] == "split":
            temp2 = []
            for j in shares:
                temp2.append(j / int(temp[1]))
            shares = temp2
        elif temp[0] == "merge":
            temp2 = []
            for j in range(int(len(shares) / int(temp[1]))):
                temp2.append(sum(shares[j * int(temp[1]):(j + 1) * int(temp[1])]))
            if len(shares) % int(temp[1]) != 0:
                temp2.append(sum(shares[int(len(shares) / int(temp[1])) * int(temp[1]):]))
            shares = temp2
        else:
            shares = [int(temp[1]) - i for i in shares]
    print(sum(shares) / len(shares))


main()
