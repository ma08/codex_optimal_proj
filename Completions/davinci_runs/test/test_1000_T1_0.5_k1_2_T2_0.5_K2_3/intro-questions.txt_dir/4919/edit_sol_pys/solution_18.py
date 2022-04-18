n = int(input())  # number of lines
trips = {}  # dictionary
for i in range(n):
    country, year = input().split()  # input country and year
    if country in trips:
        trips[country].append(int(year))  # add year to country list
    else:
        trips[country] = [int(year)]  # create country and year list

q = int(input())  # number of lines
for i in range(q):
    country, k = input().split()  # input country and k
    print(sorted(trips[country])[int(k)-1])  # print kth year
