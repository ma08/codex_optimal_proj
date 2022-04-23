
N = int(input())

div_3 = N//3
div_5 = N//5
div_15 = N//15

sum_3 = 3*div_3*(div_3+1)//2
sum_5 = 5*div_5*(div_5+1)//2
sum_15 = 15*div_15*(div_15+1)//2

print(sum_3+sum_5-sum_15)
