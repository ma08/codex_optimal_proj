#-----import-----
import sys

#-----main-----
s = sys.stdin.readline().strip()

#-----P-----
p = []
p_missing = 0
for i in range(0, len(s), 3):
    if s[i] == 'P':
        if s[i+1:i+3] not in p and s[i+1:i+3] != '00':
            p.append(s[i+1:i+3] not in p)
        else:
            print('GRESKA')
            sys.exit()
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in p and '0'+str(i) != '00':
            p_missing += 1
    else:
        if str(i) not in p and str(i) != '00':
            p_missing += 1

#-----K-----
k = []
k_missing = 0
for i in range(0, len(s), 3):
    if s[i] == 'K':
        if s[i+1:i+3] not in k and s[i+1:i+3] != '00':
            k.append(s[i+1:i+3])
        else:
            print('GRESKA')
            sys.exit()
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in k and '0'+str(i) != '00':
            k_missing += 1
    else:
        if str(i) not in k and str(i) != '00':
            k_missing += 1

#-----H-----
h = []
h_missing = 0
for i in range(0, len(s), 3):
    if s[i] == 'H':
        if s[i+1:i+3] not in h and s[i+1:i+3] != '00':
            h.append(s[i+1:i+3])
        else:
            print('GRESKA')
            sys.exit()
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in h and '0'+str(i) != '00':
            h_missing += 1
    else:
        if str(i) not in h and str(i) != '00':
            h_missing += 1

#-----T-----
t = []
t_missing = 0
for i in range(0, len(s), 3):
    if s[i] == 'T':
        if s[i+1:i+3] not in t and s[i+1:i+3] != '00':
            t.append(s[i+1:i+3])
        else:
            print('GRESKA')
            sys.exit()
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in t and '0'+str(i) != '00':
            t_missing += 1
    else:
        if str(i) not in t and str(i) != '00':
            t_missing += 1

print('{} {} {} {}'.format(p_missing, k_missing, h_missing, t_missing))
