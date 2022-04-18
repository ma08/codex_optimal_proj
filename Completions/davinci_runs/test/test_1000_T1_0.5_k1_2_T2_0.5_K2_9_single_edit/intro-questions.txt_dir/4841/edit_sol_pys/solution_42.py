

n = int(input())
counts = input().split() #inputs of numbers

if len(counts) != n:
    print("something is fishy")
    exit() #exit if number of inputs is not equal to the number declared

for i in range(n):
    if counts[i] != "mumble": #if the number is not "mumble"
        if int(counts[i]) != i + 1:
            print("something is fishy")
            exit() #exit if the number declared is not equal to the number of the input

print("makes sense")
