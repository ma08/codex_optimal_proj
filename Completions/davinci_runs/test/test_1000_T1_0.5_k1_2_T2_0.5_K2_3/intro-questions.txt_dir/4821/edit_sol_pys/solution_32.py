
#-----import-----
import sys

#-----main-----
s = sys.stdin.readline().strip() # read in input

#-----clubs-----
p = [] # list of clubs
p_missing = 0 # missing clubs
for i in range(0, len(s), 3):
    if s[i] == 'P':
        if s[i+1:i+3] not in p:
            p.append(s[i+1:i+3])
        else:
            print('GRESKA') # duplicate cards
            sys.exit() # exit program
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in p:
            p_missing += 1 # add missing card
    else:
        if str(i) not in p:
            p_missing += 1 # add missing card

#-----diamonds-----
k = [] # list of diamonds
k_missing = 0 # missing diamonds
for i in range(0, len(s), 3):
    if s[i] == 'K':
        if s[i+1:i+3] not in k:
            k.append(s[i+1:i+3])
        else:
            print('GRESKA') # duplicate cards
            sys.exit() # exit program
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in k:
            k_missing += 1 # add missing card
    else:
        if str(i) not in k:
            k_missing += 1 # add missing card

#-----hearts-----
h = [] # list of hearts
h_missing = 0 # missing hearts
for i in range(0, len(s), 3):
    if s[i] == 'H':
        if s[i+1:i+3] not in h:
            h.append(s[i+1:i+3])
        else:
            print('GRESKA') # duplicate cards
            sys.exit() # exit program
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in h:
            h_missing += 1 # add missing card
    else:
        if str(i) not in h:
            h_missing += 1 # add missing card

#-----spades-----
t = [] # list of spades
t_missing = 0 # missing spades
for i in range(0, len(s), 3):
    if s[i] == 'T':
        if s[i+1:i+3] not in t:
            t.append(s[i+1:i+3])
        else:
            print('GRESKA') # duplicate cards
            sys.exit() # exit program
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in t:
            t_missing += 1 # add missing card
    else:
        if str(i) not in t:
            t_missing += 1 # add missing card

print('{} {} {} {}'.format(p_missing, k_missing, h_missing, t_missing)) # print missing cards
