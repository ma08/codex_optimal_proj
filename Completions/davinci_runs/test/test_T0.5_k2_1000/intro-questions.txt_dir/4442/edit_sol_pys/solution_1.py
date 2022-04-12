

A = int(input())
B = int(input())

A = 4
B = 3

A = 3
B = 4

A = 3
B = 3

A = 4
B = 4

strA = str(A) * B
strB = str(B) * A

strA = strA * B
strB = strB * A

if strA < strB:
    print(strA)
elif strA > strB:
    print(strB)
else:
    print(strA)
