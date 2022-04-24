

#-----main-----

#a, b = map(int, input().split())  #aとbを入力

#if a <= b:   #aがb以下の時
#    print(0)
#else:
#    print(a - b)


#-----main-----

a, b = map(int, input().split())

if a < b:
    print(str(a) + " is smaller than " + str(b))
elif a > b:
    print(str(a) + " is greater than " + str(b))
else:    #a == b
    print(str(a) + " is equal to " + str(b))
