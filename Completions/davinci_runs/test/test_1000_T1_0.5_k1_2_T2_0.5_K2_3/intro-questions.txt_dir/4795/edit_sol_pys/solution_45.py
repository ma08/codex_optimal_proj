
N = int(input()) # Number of data points

X = 0 # Sum of the last digits

for i in range(N):
    P = input() # Data point
    X += int(P[-1]) ** int(P[0]) # Sum of the last digit raised to the power of the first digit

print(X)
