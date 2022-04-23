

#-----main-----#

a, b = map(int, input().split()) # a, b = int(input()), int(input()) でも可

if a <= b:
    print(0)
else:
    print(a - b)
