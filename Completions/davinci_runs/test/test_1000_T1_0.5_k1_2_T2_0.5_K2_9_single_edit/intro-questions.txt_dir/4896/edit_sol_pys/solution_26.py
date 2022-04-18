

N = int(input("Enter the number of bricks: "))
bricks = list(map(int, input("Enter the heights of the bricks: ").split()))

towers = 1

for i in range(1, N):
    if bricks[i] > bricks[i-1]:
        towers += 1

print("The number of towers that can be built is: ", towers)
