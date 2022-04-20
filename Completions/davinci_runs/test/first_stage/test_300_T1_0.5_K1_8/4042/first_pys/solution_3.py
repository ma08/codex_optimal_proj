

#Solution

x = float(input())

for i in range(1,11):
    for j in range(1,11):
        if i*0.1 + j*0.05 == x:
            print(i,j)
            break