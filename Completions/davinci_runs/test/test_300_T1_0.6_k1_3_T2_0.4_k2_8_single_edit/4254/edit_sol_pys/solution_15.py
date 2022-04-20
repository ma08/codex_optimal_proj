

S, W = map(int, input().split()) #input S and W
if(W >= S): #if W is greater than or equal to S, print unsafe
    print("unsafe")
else: #if W is less than S, print safe
    print("safe")
