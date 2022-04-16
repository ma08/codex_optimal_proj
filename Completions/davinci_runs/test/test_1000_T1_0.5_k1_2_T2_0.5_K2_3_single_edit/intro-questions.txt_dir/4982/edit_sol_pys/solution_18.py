

def main():
    shares = []
    for i in range(int(input())):
        temp = input().split()
        if temp[0] == "buy":  # buy 100 10
            shares.append([int(temp[1]), int(temp[2])])
        elif temp[0] == "sell":
            shares.sort(key=lambda x: x[1])
            for j in range(int(temp[1])):
                shares[j][1] = int(temp[2]) - shares[j][1]
        elif temp[0] == "split":
            temp2 = []
            for j in shares:  # j[0] is number, j[1] is price
                temp2.append([j[0]/int(temp[1]), j[1]])
            shares = temp2
        elif temp[0] == "merge":
            temp2 = []
            for j in range(int(len(shares)/int(temp[1]))):  # 100 10 200 20 -> [100, 10] [200, 20]
                temp2.append([shares[j*int(temp[1])][0] + shares[(j+1)*int(temp[1])][0], shares[j*int(temp[1])][1]])
            if len(shares)%int(temp[1]) != 0:
                temp2.append([shares[int(len(shares)/int(temp[1]))*int(temp[1])][0] + shares[-1][0], shares[-1][1]])
            shares = temp2
        else:
            for j in range(len(shares)):
                shares[j][1] = int(temp[1]) - shares[j][1]
    print(sum([i[0]*i[1] for i in shares])/sum([i[0] for i in shares]))

main()
