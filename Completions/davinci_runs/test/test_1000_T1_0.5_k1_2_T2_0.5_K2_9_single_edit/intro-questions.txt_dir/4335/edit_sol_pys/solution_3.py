

# First, get the length of the string, N.
# Second, get the string, S.
N = int(input())
S = input()

# If N is even, check if S[:N / 2] is equal to S[(N / 2):].
# If N is odd, check if S[:N / 2] is equal to S[(N / 2) + 1:].
# If either of the above conditions is true, print "Yes".
# Otherwise, print "No".
if N % 2 == 0:
    if S[:N / 2] == S[(N / 2):]:
        print("Yes")
    else:
        print("No")
else:
    if S[:N / 2] == S[(N / 2) + 1:]:
        print("Yes")
    else:
        print("No")
