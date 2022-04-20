

# SOLUTION

n = int(input())
s = input()

if s.count('xxx') == 0:
    print(0)
else:
    print(s.count('x') - s.count('xxx') + 1)