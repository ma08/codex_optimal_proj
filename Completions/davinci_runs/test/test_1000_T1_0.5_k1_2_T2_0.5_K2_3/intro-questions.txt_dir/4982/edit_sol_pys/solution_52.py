

def main():
    # read the input file
    f = open("grumpy_old_cat.txt","r")
    # get the lines
    lines = f.readlines()
    # initialize the total number of shares
    total_shares = 0
    # initialize the average cost per share and the total cost
    average_cost, total_cost = 0, 0
    # initialize the stock price
    stock_price = 0
    # iterate through the lines
    for line in lines:
        # split the line into a list
        line_list = line.split()
        # if the line starts with "buy"
        if line_list[0] == "buy":
            # update the total number of shares
            total_shares += int(line_list[1])
            # update the average cost per share and the total cost
            total_cost += int(line_list[1])*int(line_list[2])
            average_cost = total_cost/total_shares
        # if the line starts with "sell"
        elif line_list[0] == "sell":
            # update the total number of shares
            total_shares -= int(line_list[1])
        # if the line starts with "split"
        elif line_list[0] == "split":
            # update the total number of shares
            total_shares *= int(line_list[1])
            # update the average cost per share
            average_cost /= int(line_list[1])
        # if the line starts with "merge"
        elif line_list[0] == "merge":
            # update the total number of shares
            total_shares = total_shares//int(line_list[1])
            # update the average cost per share
            average_cost = average_cost*int(line_list[1])
        # if the line starts with "die"
        elif line_list[0] == "die":
            # update the stock price
            stock_price = int(line_list[1])
    # calculate the final sale
    final_sale = total_shares*(stock_price - average_cost*0.3)
    # print the final sale
    print("%.8f" % final_sale)

main()
