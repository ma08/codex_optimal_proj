
# Get Input
N = int(input())

# Check if Even or Odd
if N % 2 == 0 and (N > 2 and N < 5):
    print("Not Weird")
elif N % 2 == 0 and (N > 6 and N <= 20):
    print("Weird")
elif N % 2 == 0 and N > 20:
    print("Even")
elif N % 2 != 0:
    print("Odd")
