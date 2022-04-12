

#inputs
a, b = map(int, input().split())
m, sigma = map(int, input().split())

#initialize max rent
max_rent = 0

#loop through each possible x
for x in range(1, m//2 + 1):
    #calculate y
    y = m - x
    #check if the number of outlets is satisfied
    if(2*x + y >= sigma):
        #calculate rent
        rent = a*x + b*y
        #if rent is greater than max rent
        if(rent > max_rent):
            #update max rent
            max_rent = rent

#output
print(max_rent)
