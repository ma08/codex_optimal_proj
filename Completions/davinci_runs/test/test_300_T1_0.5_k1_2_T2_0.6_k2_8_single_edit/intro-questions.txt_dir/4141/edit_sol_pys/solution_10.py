
n = int(input())
for i in range(n):
    num = int(input())
    if num % 2 == 0 and num % 3 != 0 and num % 5 != 0:
        print("DENIED")
    else:
        print("APPROVED")
