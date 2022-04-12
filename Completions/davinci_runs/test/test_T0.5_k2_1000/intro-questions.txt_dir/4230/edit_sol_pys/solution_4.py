x = int(input().split()[0]) #x is the number of the house
n = int(input().split()[0]) #n is the number of the houses
p = [int(i) for i in input().split()] #p is the list of the houses
p.sort() #sort the list

if x <= p[0]:
    print(p[0]-x)
elif x >= p[-1]:
    print(x-p[-1])
else:
    for i in range(1, n):
        if x <= p[i]:
            print(min(x-p[i-1], p[i]-x))
            break
