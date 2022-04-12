

# Get the length of the string, N.
N = int(input())

# If N is even, print "Yes" if S[:N//2] is equal to S[N//2:].
# If N is odd, print "Yes" if S[:N//2] is equal to S[(N//2)+1:].
# Otherwise, print "No". 
if N % 2 == 0:
    if input()[:N//2] == input()[N//2:]:
        print("Yes")
    else:
        print("No")
else:
    if input()[:N//2] == input()[(N//2)+1:]:
        print("Yes")
    else:
        print("No")
