
#-----main-----
s = input()

#najdi nejvetsi ctverec
max_ctv = int(len(s)**0.5) + 1
#vypis v ctvercich zprava doleva
for i in range(max_ctv,0,-1):
    if len(s) % i == 0:
        #vypis zprava doleva
        for j in range(0,len(s),i):
            print(s[j:j+i])
        break
