

#-----main-----#

s = input()

#find the biggest square
max_sq = int(len(s)**0.5)

#print in square
for i in range(max_sq,0,-1):
    if len(s) % i == 0:
        #print from left to right
        for j in range(0,len(s),i):
            print(s[j:j+i])
        break
