import os
import csv

csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(header)

    months = []
    profits = []
    previous_profit = 0
    profit_change = []
    avg_change = 0
    max_change = 0
    min_change = 0
    
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))
        current_profit = int(row[1])
        change = current_profit - previous_profit
        previous_profit = current_profit
        profit_change.append(change)
        if change > max_change:
            max_change = change
            max_month = row[0]
        elif change < min_change:
            min_change = change
            min_month = row[0]

    profit_change.pop(0)
    avg_change = sum(profit_change)/len(profit_change)

    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total: ${sum(profits)}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {max_month} (${max_change})')
    print(f'Greatest Decrease in Profits: {min_month} (${min_change})')

output_path = os.path.join('..', 'PyBank', 'Analysis', 'financial_analysis.txt')
with open(output_path, 'w') as file:
    file.write('Financial Analysis\n')
    file.write('----------------------------\n')
    file.write(f'Total Months: {len(months)}\n')
    file.write(f'Total: ${sum(profits)}\n')
    file.write(f'Average Change: ${avg_change}\n')
    file.write(f'Greatest Increase in Profits: {max_month} (${max_change})\n')
    file.write(f'Greatest Decrease in Profits: {min_month} (${min_change})\n')
    file.close()
