

e,f,c = map(int,input().split()) #take input from user and store in e f and c

bottles = e + f #total no of bottles
drinks = 0 #no of drinks

while bottles >= c:
    drinks += bottles // c
    bottles = bottles % c + bottles // c

print(drinks)
