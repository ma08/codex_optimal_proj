

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())

increasing = True
decreasing = True
for i in range(1, n):
    if names[i - 1] < names[i]:
        decreasing = False
    elif names[i - 1] > names[i]:
        increasing = False

if increasing:
    print("INCREASING")
elif decreasing:
    print("DECREASING")
else:
    print("NEITHER")
