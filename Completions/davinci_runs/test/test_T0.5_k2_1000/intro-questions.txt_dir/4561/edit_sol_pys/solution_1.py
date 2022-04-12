
# input
X, A, B = map(int, input().split())

# output
if A >= B:
    print("delicious")
elif B < (X - A):
    print("dangerous")
else:
    print("safe")
