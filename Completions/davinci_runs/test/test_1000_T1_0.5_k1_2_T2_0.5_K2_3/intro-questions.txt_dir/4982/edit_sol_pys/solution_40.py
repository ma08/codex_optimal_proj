

def main():
    # read the input file
    f = open("grumpy_old_cat.txt","r") # open the file
    # get the lines
    lines = f.readlines() # read all the lines
    # initialize the total number of shares
    total_shares = 0 # initialize the total number of shares
    # initialize the average cost per share
    average_cost = 0 # initialize the average cost per share
    # initialize the stock price
    stock_price = 0 # initialize the stock price
    # iterate through the lines
    for line in lines: # iterate through the lines
        # split the line into a list
        line_list = line.split() # split the line into a list
        # if the line starts with "buy"
        if line_list[0] == "buy": # if the line starts with "buy"
            # update the total number of shares
            total_shares += int(line_list[1]) # update the total number of shares
            # update the average cost per share
            average_cost = (average_cost*(total_shares-int(line_list[1]))+int(line_list[1])*int(line_list[2]))/total_shares # update the average cost per share
        # if the line starts with "sell"
        elif line_list[0] == "sell": # if the line starts with "sell"
            # update the total number of shares
            total_shares -= int(line_list[1]) # update the total number of shares
        # if the line starts with "split"
        elif line_list[0] == "split": # if the line starts with "split"
            # update the total number of shares
            total_shares *= int(line_list[1]) # update the total number of shares
            # update the average cost per share
            average_cost /= int(line_list[1]) # update the average cost per share
        # if the line starts with "merge"
        elif line_list[0] == "merge": # if the line starts with "merge"
            # update the total number of shares
            total_shares = total_shares//int(line_list[1]) # update the total number of shares
            # update the average cost per share
            average_cost = average_cost*int(line_list[1]) # update the average cost per share
        # if the line starts with "die"
        elif line_list[0] == "die": # if the line starts with "die"
            # update the stock price
            stock_price = int(line_list[1]) # update the stock price
    # calculate the final sale
    final_sale = total_shares*(stock_price - average_cost*0.3) # calculate the final sale
    # print the final sale
    print("%.8f" % final_sale) # print the final sale

main() # call the main function
