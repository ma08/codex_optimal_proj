

n, d_m = map(int, input().split()) # n is the number of days, and d_m is the day of the month
d_list = list(map(int, input().split())) # d_list is a list of the days of the month that it snowed

k = 0
while k < n and d_list[k] > d_m: # iterate through the list of days it snowed
    k += 1

if k == 0: # if it never snowed before the given day
    print("It had never snowed this early!")
else: # otherwise, it snowed before the given day
    print("It hadn't snowed this early in {} years!".format(k))
