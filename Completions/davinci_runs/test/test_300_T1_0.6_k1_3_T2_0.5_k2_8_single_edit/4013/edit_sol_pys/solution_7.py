n = int(input("Enter number of numbers: "))
sum = 0
for i in range(n):
    num = int(input("Enter number: "))
    sum += num
print(sum)
if sum > 100:
    print("You win")
else:
    print("You lose")
