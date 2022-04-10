

#-----Main-----

a = int(input())

print(a - int(bin(a)[2:].count('1')))