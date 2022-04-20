

#-----main-----
s = input()
n = len(s)

#-----function-----
def two_gram(s,n):
    l = []
    for i in range(n-1):
        l.append(s[i:i+2])
    return l

def check_max(l):
    m = 0
    for i in l:
        if l.count(i) > m:
            m = l.count(i)
    return m

def print_max(l,m):
    for i in l:
        if l.count(i) == m:
            print(i)
            break

#-----process-----
l = two_gram(s,n)
m = check_max(l)
print_max(l,m)