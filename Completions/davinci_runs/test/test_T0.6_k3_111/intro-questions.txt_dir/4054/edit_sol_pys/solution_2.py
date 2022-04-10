

n = [int(i) for i in input().split()]  # input list of numbers

# Find the least common multiple
lcm = n[0]  # set lcm to first number in list
for i in n:  # loop through list
    while lcm % i != 0:  # while lcm is not divisible by i
        lcm += 1  # increment lcm by 1

print(lcm)  # print lcm
