
def sum_of_multiples(n):
    div3 = n//3
    div5 = n//5
    div15 = n//15
    sum3 = 3*div3*(div3+1)//2
    sum5 = 5*div5*(div5+1)//2
    sum15 = 15*div15*(div15+1)//2
    return sum3+sum5-sum15
print(sum_of_multiples(1000))
