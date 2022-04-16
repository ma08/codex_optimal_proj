
def main():
    shares = []
    for i in range(int(input())):
        temp = input().split() # get input
        if temp[0] == "buy":
            shares.append(int(temp[1]) * int(temp[2]))
        elif temp[0] == "sell":
            shares.sort()
            for j in range(int(temp[1])):
                shares[j] = int(temp[2]) - shares[j]
        elif temp[0] == "split":
            shares = [j/int(temp[1]) for j in shares]
        elif temp[0] == "merge":
            shares = [sum(shares[j*int(temp[1]):(j+1)*int(temp[1])]) for j in range(int(len(shares)/int(temp[1])))]
            if len(shares)%int(temp[1]) != 0:
                shares.append(sum(shares[int(len(shares)/int(temp[1]))*int(temp[1]):]))
        else:
            shares = [int(temp[1]) - i for i in shares]
    print(sum(shares)/len(shares))

main()
