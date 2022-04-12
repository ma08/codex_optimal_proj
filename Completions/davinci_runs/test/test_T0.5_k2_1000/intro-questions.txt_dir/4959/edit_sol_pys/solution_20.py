

e,f,c = map(int,input().split()) #e=empty bottles, f=full bottles, c=capacity of bottles 

bottles = e + f #total bottles
drinks = 0

while bottles >= c:
    drinks += bottles // c
    bottles = bottles % c + bottles // c

print(drinks)
