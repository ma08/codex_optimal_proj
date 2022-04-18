

# Greedy Algorithm

t = int(input()) #number of test cases

for _ in range(t):
    n = int(input()) #number of activities
    a = []
    for __ in range(n):
        a.append(list(map(int, input().split()))) #starting time and ending time
    a.sort(key=lambda x: x[1]) #sort by ending time
    count = 0 #initialize count
    j = 0
    for i in range(n):
        if a[i][0] >= a[j][1]: #if starting time of activity i is greater than ending time of activity j
            count += 1
            j = i #end time of activity i becomes the new end time
    print(count)
