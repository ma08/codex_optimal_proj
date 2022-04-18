
#-----main-----

s = input()

#najdi nejveci ctverec
max_ctv = int(len(s)**0.5)

#vypis v ctverecich
for i in range(max_ctv,0,-1):
    if len(s) % i == 0:
        #vypis zleva do prava
        for j in range(0,len(s),i):
            print(s[j:j+i])
        break
