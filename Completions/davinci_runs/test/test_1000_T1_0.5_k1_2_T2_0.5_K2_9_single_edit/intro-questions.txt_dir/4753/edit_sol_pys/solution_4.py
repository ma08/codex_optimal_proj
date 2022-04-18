
n = int(input())

if n < 3 or n > 100:
    raise ValueError("Input is out of range.")

print((n-3)*(n-2)*(n-1)//6)  # print number of possible triangles
