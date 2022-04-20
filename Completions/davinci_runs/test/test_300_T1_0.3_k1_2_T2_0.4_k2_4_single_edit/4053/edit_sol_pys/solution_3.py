

n = int(input())
prefixes = []
suffixes = []

for i in range(2*n-2):
    s = input()
    if len(s) == 1:
        prefixes.append(s)
    else:
        suffixes.append(s)

for i in range(2*n-2):
    if i < n-1 and prefixes[i] == 'P':
    elif i < n-1 and prefixes[i] == 'S':
        print("S", end="")
    elif i >= n-1 and suffixes[i-n+1] == 'P':
        print("P", end="")
        print("P", end="")
    else:





        print("S", end="")
