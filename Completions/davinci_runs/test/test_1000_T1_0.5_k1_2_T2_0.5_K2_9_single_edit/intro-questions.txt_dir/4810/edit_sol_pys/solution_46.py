

#-----main-----

s = input()

#najdi nejveci ctverec
max_ctv = int(round(len(s)**0.5))

#vypis v ctvercich
for i in range(max_ctv,0,-1): #od max_ctv po 1
    if len(s) % i == 0:
        #vypis zleva do prava
        for j in range(0,len(s),i): #od 0 po delku s krokem i
            print(s[j:j+i]) #vypis z j po j+i
        break
