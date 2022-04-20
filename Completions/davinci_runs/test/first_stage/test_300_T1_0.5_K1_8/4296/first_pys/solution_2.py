

#get input
str_input = input().split()

#convert input to integers
int_input = [int(i) for i in str_input]

#sum input
sum_input = sum(int_input)

#print
if sum_input >= 22:
    print("bust")
else:
    print("win")