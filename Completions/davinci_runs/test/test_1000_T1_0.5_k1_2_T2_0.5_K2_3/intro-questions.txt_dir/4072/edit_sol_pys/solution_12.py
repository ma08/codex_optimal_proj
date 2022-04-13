

# Write your code here
n = int(input())
for i in range(n):
    a = int(input())
    if a % 10 == 0 or a % 10 == 7 or a % 10 == 1:
        print(1)
    else:
        print(0)
