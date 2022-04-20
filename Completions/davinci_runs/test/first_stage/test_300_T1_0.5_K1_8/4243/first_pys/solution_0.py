

import math

x = int(input())

fivehundred = math.floor(x/500)
hundred = math.floor((x%500)/100)
fifty = math.floor((x%500%100)/50)
ten = math.floor((x%500%100%50)/10)
five = math.floor((x%500%100%50%10)/5)
one = math.floor((x%500%100%50%10%5)/1)

print(fivehundred*1000 + hundred*100 + fifty*50 + ten*10 + five*5 + one*1)