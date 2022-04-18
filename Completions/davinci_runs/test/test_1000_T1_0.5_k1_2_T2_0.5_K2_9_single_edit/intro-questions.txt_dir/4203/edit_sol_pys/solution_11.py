
S = str(input())
if S[0] == 'A' and S[2:-1].count('C') == 1:
    for i in range(2, len(S) - 1):
        if S[i] == 'C': continue
        elif S[i].islower(): continue
        else: print('WA'); exit()
    print('AC')
else:
    print('WA')
