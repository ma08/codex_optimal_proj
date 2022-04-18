

n, m, s, d = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

# First, we check if it is possible, i.e.
# all the slots are full, and the number of
# cold sodas is less than the number of students
# that need to be served
if sum(c) < m:
    print("impossible")
    exit()

# We need to find a way to maximize the probability
# that the next m students receive a cold soda.
# We can do this by minimizing the probability that
# a student receives a hot soda.
#
# We can calculate the probability of receiving a
# hot soda by dividing the number of hot sodas by
# the total number of sodas.
#
# We can minimize this probability by making the
# number of hot sodas as small as possible, while
# making the number of total sodas as large as possible.
#
# Suppose we have the following fridge:
# [0, 1, 4]
# If we put the new sodas in slot 0, then the
# probability of receiving a hot soda is 5/9.
# If we put the new sodas in slot 1, then the
# probability of receiving a hot soda is 4/8.
# If we put the new sodas in slot 2, then the
# probability of receiving a hot soda is 1/5.
#
# We can see that the best place to put the new sodas
# is in slot 2, since it has the minimum probability
# of receiving a hot soda.
#
# In general, we can see that the best place to put the
# new sodas is in the slot that has the minimum number
# of hot sodas, and is not full.
#
# We can calculate the number of hot sodas in a slot
# by taking the difference between the number of sodas
# in the slot, and the number of cold sodas in the slot.
#
# We can calculate the number of total sodas in a slot
# by taking the sum of the number of cold sodas in the slot,
# and the number of new sodas in the slot.
#
# When we place the new sodas in a slot, we need to make
# sure that there are still enough new sodas left to fill
# the other slots.
#
# We can do this by checking that the number of new sodas
# that we want to place in a slot is less than or equal
# to the number of new sodas left to place.

# First, we initialize the number of new sodas left to place
# as the number of new sodas
new_sodas_left = n

# We also initialize the number of hot sodas in a slot
# as the difference between the number of sodas in a slot,
# and the number of cold sodas in a slot
hot_sodas_in_slot = [d - c[i] for i in range(s)]

# We also initialize the number of total sodas in a slot
# as the sum of the number of cold sodas in a slot,
# and the number of new sodas in a slot
total_sodas_in_slot = [c[i] for i in range(s)]

# We also initialize the number of new sodas to place in a slot
# as 0
new_sodas_in_slot = [0 for i in range(s)]

# We will put the new sodas in the slots in ascending order
# of the number of hot sodas in the slot, so we sort the
# list of hot sodas in the slot
hot_sodas_in_slot, total_sodas_in_slot, new_sodas_in_slot = zip(*sorted(zip(hot_sodas_in_slot, total_sodas_in_slot, new_sodas_in_slot)))

# Next, we iterate over the slots in ascending order
# of the number of hot sodas in the slot
for i in range(s):
    # We check if the slot is not full
    if c[i] < d:
        # We check if there are enough new sodas left to fill
        # the slot
        if new_sodas_left >= d - c[i]:
            # If there are enough new sodas left to fill the slot,
            # we set the number of new sodas in the slot as the
            # difference between the capacity of the slot, and the
            # number of sodas in the slot
            new_sodas_in_slot[i] = d - c[i]
            # We also update the number of new sodas left to place
            new_sodas_left -= new_sodas_in_slot[i]
            # We also update the number of hot sodas in the slot
            hot_sodas_in_slot[i] = 0
            # We also update the number of total sodas in the slot
            total_sodas_in_slot[i] = d
        else:
            # If there are not enough new sodas left to fill the slot,
            # we set the number of new sodas in the slot as the number
            # of new sodas left to place
            new_sodas_in_slot[i] = new_sodas_left
            # We also update the number of new sodas left to place
            new_sodas_left = 0
            # We also update the number of hot sodas in the slot
            hot_sodas_in_slot[i] = hot_sodas_in_slot[i] - new_sodas_in_slot[i]
            # We also update the number of total sodas in the slot
            total_sodas_in_slot[i] = total_sodas_in_slot[i] + new_sodas_in_slot[i]

# We print the number of new sodas in the slot
print(*new_sodas_in_slot)
