

#input
a, b = map(int, input().split())
n, sigma = map(int, input().split())

#initialize max revenue
max_revenue = 0

#loop through each possible x
for x in range(1, n//2 + 1):
    #calculate y
    y = n - x
    #check if the number of outlets is satisfied
    if(2*x + y >= sigma):
        #calculate rent
        rent = a*x + b*y
        if(rent > max_revenue):
            #update max revenue
            max_revenue = rent

#output
print(max_revenue)
