
A, B = map(int, input().split()) #split the input by space

if A * B % 2 == 0: #if the product of A and B is even
    print("Even")
else:
    print("Odd")
