

A = int(input())
B = int(input())

strA = str(A)
strB = str(B)

strA = strA * B
strB = strB * A

if strA < strB:
    print(strA)
elif strA > strB:
    print(strB)
else:
    print(strA)
