

n = int(input())

for i in range(n//4+1):
    for j in range(n//7+1):
        if n == i*4 + j*7: print("Yes"); exit()
print("No") 
