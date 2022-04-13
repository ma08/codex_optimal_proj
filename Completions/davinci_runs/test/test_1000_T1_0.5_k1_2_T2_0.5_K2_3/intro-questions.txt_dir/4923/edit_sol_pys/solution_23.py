
n = int(input())
rolls = [int(x) for x in input().split()]
highest = 0
winner = None
for index, roll in enumerate(rolls):
    if roll > highest:
        if rolls.count(roll) == 1:  # count how many times the roll is repeated
            highest = roll
            winner = index
if winner is None:
    print("none")
else:
    print(winner+1)
