

n, m = map(int, input().split())  # n = number of cups, m = number of pages
a = list(map(int, input().split()))  # a = list of pages per cup

a.sort()

cups = 0  # number of cups used
pages = 0  # number of pages used
days = 0  # number of days

while cups < n:
    pages += a[cups]  # add pages of current cup
    days += 1  # add 1 day
    cups += 1  # add 1 cup
    if pages >= m:  # if pages is greater than or equal to m, break
        break
    if cups < n:  # if cups is less than n, subtract days - 1
        pages -= days - 1  # this is to ensure that the pages of the current cup is not included

if pages < m:  # if pages is less than m, days is -1
    days = -1

print(days)
