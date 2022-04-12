

#-----import------
import sys

#-----main-----
s = sys.stdin.readline().strip().split(' ')

#-----check-----
for i in range(len(s)):
    if len(s[i]) != 3:
        print('GRESKA')
        sys.exit()
    if s[i][0] not in 'PKHT':
        print('GRESKA')
        sys.exit()
    if s[i][1:3] not in '0123456789':
        print('GRESKA')
        sys.exit()
    if int(s[i][1:3]) > 13 or int(s[i][1:3]) < 1:
        print('GRESKA')
        sys.exit()

#-----P-----
p = []
p_missing = 0
for i in range(len(s)):
    if s[i] == 'P':
        if s[i+1:i+3] not in p:
            p.append(s[i+1:i+3])
        else:
            print('GRESKA')
            sys.exit()
for i in range(1, 14):
    if len(str(i)) == 1:
        if '0'+str(i) not in p:
            p_missing += 1
    else:
        if str(i) not in p:
            p_missing += 1

#-----K-----
k = []
k_missing = 0
for i in range(len(s)):
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

#-----H-----
h = []
h_missing = 0
for i in range(len(s)):
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

#-----T-----
t = []
t_missing = 0
for i in range(len(s)):
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
