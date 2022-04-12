

#-----main-----#

s = input()

#najdi nejveci ctvercovy podretezec
max_ctv = int(len(s)**0.5) + 1

#vypis v ctvercich zleva do prava
for i in range(max_ctv,0,-1):
    if len(s) % i == 0:
        for j in range(0,len(s),i):
            print(s[j:j+i])
        break
