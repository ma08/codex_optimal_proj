import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(f"CSV Header: {header}")

    month_count = 0
    total_profit = 0
    profit_list = []
    month_list = []
    change_list = []

    # Loop through the data
    for row in csvreader:
        month_count = month_count + 1
        total_profit = total_profit + int(row[1])
        profit_list.append(row[1])
        month_list.append(row[0])

    for i in range(1,len(profit_list)):
        change_list.append(int(profit_list[i]) - int(profit_list[i-1]))
        avg_change = sum(change_list)/len(change_list)
        max_change = max(change_list)
        min_change = min(change_list)
        max_month = month_list[change_list.index(max(change_list)) + 1]
        min_month = month_list[change_list.index(min(change_list)) + 1]

    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(month_count))
    print("Total: $" + str(total_profit))
    print("Average Change: $" + str(round(avg_change,2)))
    print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_change) + ")")
    print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_change) + ")")

with open("financial_analysis.txt", "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("-------------------------", file=text_file)
    print("Total Months: " + str(month_count), file=text_file)
    print("Total: $" + str(total_profit), file=text_file)
    print("Average Change: $" + str(round(avg_change,2)), file=text_file)
    print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_change) + ")", file=text_file)
    print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_change) + ")", file=text_file)
