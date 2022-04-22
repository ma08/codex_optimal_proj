


l = int(input())
x = [int(i) for i in input().split()]

for i in range(l):
    if x[i] == 1:
        print("HARD")
        exit()

print("EASY")
