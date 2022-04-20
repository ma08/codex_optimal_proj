

# Get input
n = int(input()) # number of immigrants
a = list(map(int, input().split())) # list of ages

# Check if the immigrant should be allowed entry
for i in range(n):
    if a[i] % 2 == 0 and a[i] % 3 != 0 and a[i] % 5 != 0:
        print("DENIED")
        break
else:
    print("APPROVED")
