

s = str(input())

print(max(s.count('RR'), s.count('R') - 1, s.count('R')))
