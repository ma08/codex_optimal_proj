

n = int(input())
arr = list(map(int, input().split()))

# min:
# If all people stay, there will be n houses.
# If all people move, there will be 2 houses.
# If all people move except one, there will be 3 houses.
# If all people move except two, there will be 4 houses.
# If all people move except three, there will be 5 houses.
# If all people move except four, there will be 6 houses.

# max:
# If all people stay, there will be n houses.
# If all people move, there will be 2 houses.
# If all people move except one, there will be 3 houses.
# If all people move except two, there will be 4 houses.
# If all people move except three, there will be 5 houses.
# If all people move except four, there will be 6 houses.

# If the number of people is even, then the minimum number of houses is 2.
# If the number of people is odd, then the minimum number of houses is 3.

# If the number of people is even, then the maximum number of houses is n.
# If the number of people is odd, then the maximum number of houses is n + 1.

min_houses = 2
max_houses = n

if n % 2 == 1:
    min_houses = 3
    max_houses = n + 1

print(min_houses, max_houses)