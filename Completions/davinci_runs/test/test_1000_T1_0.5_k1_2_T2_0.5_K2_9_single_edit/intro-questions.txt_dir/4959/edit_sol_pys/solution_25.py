
e,f,c = map(int,input().split())

bottles = e + f
drinks = bottles

while bottles >= c:
    drinks += bottles // c - 1
    bottles = bottles % c + bottles // c


print(drinks)
