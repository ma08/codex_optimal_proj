
s = input()[::-1]
print('Yes' if (len(s) % 2 == 0) and (s[0] in 'RDL') and (s[-1] in 'RDL') else 'No')
