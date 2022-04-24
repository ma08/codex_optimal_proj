

# Solved by Tashfia Rahman 

n = int(input()) # number of soldiers

attack = list(map(int, input().split())) # attack power
defend = list(map(int, input().split())) # defense power

attack.sort(reverse=True) # sort the attack power in descending order
defend.sort(reverse=True) # sort the defense power in descending order

sum = 0 # initialize sum

for i in range(n): # iterate through all soldiers
    if attack[i] > defend[i]: # if attack power of a soldier is greater than defense power of a soldier
        sum = sum + defend[i] # add defense power to the sum
    else: # if attack power of a soldier is not greater than defense power of a soldier
        sum = sum + attack[i] # add attack power to the sum

print(sum) # print the sum
