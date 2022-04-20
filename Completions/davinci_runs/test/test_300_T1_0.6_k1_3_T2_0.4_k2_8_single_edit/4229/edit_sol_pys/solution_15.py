





N = int(input())

div3 = N//3
div5 = N//5
div15 = N//15

sum3 = 3*div3*(div3+1)//2
sum5 = 5*div5*(div5+1)//2
sum15 = 15*div15*(div15+1)//2

print(sum3+sum5-sum15)
