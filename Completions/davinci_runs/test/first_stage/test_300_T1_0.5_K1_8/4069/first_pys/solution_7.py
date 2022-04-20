

#import numpy as np

#X, K, D = map(int, input().split())
#X = int(input())
#K = int(input())
#D = int(input())

X = 6
K = 2
D = 4

#if (X >= 0):
#    if (K*D <= X):
#        print(X-K*D)
#    elif (K*D > X):
#        print(abs(X-K*D)%D)
#elif (X < 0):
#    if (K*D <= abs(X)):
#        print(abs(X+K*D))
#    elif (K*D > abs(X)):
#        print(abs(X+K*D)%D)

#if (X >= 0):
#    if (K*D <= X):
#        print(X-K*D)
#    elif (K*D > X):
#        print(abs(X-K*D)%D)
#elif (X < 0):
#    if (K*D <= abs(X)):
#        print(abs(X+K*D))
#    elif (K*D > abs(X)):
#        print(abs(X+K*D)%D)

if (X >= 0):
    if (K*D <= X):
        print(X-K*D)
    elif (K*D > X):
        print(abs(X-K*D)%D)
elif (X < 0):
    if (K*D <= abs(X)):
        print(abs(X+K*D))
    elif (K*D > abs(X)):
        print(abs(X+K*D)%D)

#if (X >= 0):
#    if (K*D <= X):
#        print(X-K*D)
#    elif (K*D > X):
#        print(abs(X-K*D)%D)
#elif (X < 0):
#    if (K*D <= abs(X)):
#        print(abs(X+K*D))
#    elif (K*D > abs(X)):
#        print(abs(X+K*D)%D)