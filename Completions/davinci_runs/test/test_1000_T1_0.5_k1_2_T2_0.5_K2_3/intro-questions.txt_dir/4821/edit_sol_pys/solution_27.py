

#-----import-----
import sys

#-----main-----
s = sys.stdin.readline().strip() # read string

#-----clubs-----
p = [] # clubs
p_missing = 0 # clubs missing
for i in range(0, len(s), 3):
    if s[i] == 'P':
        if s[i+1:i+3] not in p:
            p.append(s[i+1:i+3])
        else:
            print('GRESKA')
            sys.exit() # exit if error
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in p:
            p_missing += 1
    else:
        if str(i) not in p:
            p_missing += 1

#-----diamonds-----
k = [] # diamonds
k_missing = 0 # diamonds missing
for i in range(0, len(s), 3):
    if s[i] == 'K':
        if s[i+1:i+3] not in k:
            k.append(s[i+1:i+3])
        else:
            print('GRESKA')
            sys.exit()
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in k:
            k_missing += 1
    else:
        if str(i) not in k:
            k_missing += 1

#-----hearts-----
h = []
h_missing = 0
for i in range(0, len(s), 3):
    if s[i] == 'H':
        if s[i+1:i+3] not in h:
            h.append(s[i+1:i+3])
        else:
            print('GRESKA')
            sys.exit()
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in h:
            h_missing += 1
    else:
        if str(i) not in h:
            h_missing += 1

#-----spades-----
t = []
t_missing = 0
for i in range(0, len(s), 3):
    if s[i] == 'T':
        if s[i+1:i+3] not in t:
            t.append(s[i+1:i+3])
        else:
            print('GRESKA')
            sys.exit()
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in t:
            t_missing += 1
    else:
        if str(i) not in t:
            t_missing += 1

print('{} {} {} {}'.format(p_missing, k_missing, h_missing, t_missing))
