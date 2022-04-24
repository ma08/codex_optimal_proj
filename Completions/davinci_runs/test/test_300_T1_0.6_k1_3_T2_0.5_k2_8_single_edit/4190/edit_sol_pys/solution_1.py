

#-----Solution-----

def main():
    n = int(input()) # number of elements
    a = list(map(int, input().split())) # list A
    b = list(map(int, input().split())) # list B
    c = [] # list C
    for i in range(n): # append list C with sum of A and B
        c.append(a[i]+b[i]) 

    c.sort() # sort list C
    l = [] # list L
    for i in range(n): # append list L with modulus of C and n
        l.append(c[i]%n) 

    print(*l)

main()
