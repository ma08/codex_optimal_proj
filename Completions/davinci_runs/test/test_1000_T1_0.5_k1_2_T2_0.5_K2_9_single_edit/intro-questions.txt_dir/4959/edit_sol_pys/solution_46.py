print "How many bottles do you have?"
a = raw_input()
print "How many empty bottles do you have?"
b = raw_input()
print "How many bottles do you need to buy a new one?"
c = raw_input()
soda = 0
empty = int(a) + int(b)
while empty >= int(c):
    empty = empty - int(c) + 1
    soda += 1
print soda
# This is the code without the input
'''

a = map(int, raw_input().split())
soda = 0
empty = a[0] + a[1]
while empty >= a[2]:
    empty = empty - a[2] + 1
    soda += 1
'''
print soda
