

r, c, zr, zc = map(int, input().split()) #get input

article = [] #define a list
for i in range(r):
    article.append(input()) #append the input to the list

for i in range(r): #print the list
    for j in range(zr): #print the list in a zr x zc matrix
        for k in range(c): #print the list in a zr x zc matrix
            for l in range(zc): #print the list in a zr x zc matrix
                print(article[i][k], end="") #print the list in a zr x zc matrix
        print()
