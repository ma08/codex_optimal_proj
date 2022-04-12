

#input
a, b = map(int, input().split())
m, sigma = map(int, input().split())

#initialize max revenue
max_revenue = 0

#loop through each possible x
for x in range(1, m//2 + 1):
    #calculate y
    y = m - x
    #check if the number of outlets is satisfied
    if(2*x + y >= sigma):
        #calculate rent
        rent = a*x + b*y
        if(rent > max_revenue):
            #update max revenue
            max_revenue = rent

#output
print(max_revenue)
