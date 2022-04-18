

# Get the length of the string, N.
N = int(input())

# If N is even, print "Not Weird".
if N % 2 == 0 and 2 <= N <= 5:
    print("Not Weird")
# If N is even, print "Weird".
elif N % 2 == 0 and 6 <= N <= 20:
    print("Weird")
# If N is even, print "Not Weird".
elif N % 2 == 0 and N > 20:
    print("Not Weird")
# If N is odd, print "Weird".
else:
    print("Weird")
