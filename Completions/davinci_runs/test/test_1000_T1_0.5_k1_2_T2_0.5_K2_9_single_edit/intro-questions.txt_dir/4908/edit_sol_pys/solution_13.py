

import sys

# Read the numbers
nums = sys.stdin.readline().split()
nums = [int(num) for num in nums]

# Compute the possible answers
answers = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            if i < 2:
                a = eval(str(nums[0]) + ["+", "-"][i] + str(nums[1]))
            else:
                a = eval(str(nums[0]) + ["*", "/"][i-2] + str(nums[1]))
            if j < 2:
                b = eval(str(a) + ["+", "-"][j] + str(nums[2]))
            else:
                b = eval(str(a) + ["*", "/"][j-2] + str(nums[2]))
            if k < 2:
                c = eval(str(b) + ["+", "-"][k] + str(nums[3]))
            else:
                c = eval(str(nums[0]) + ["*", "/"][k-2] + str(b))
            if c == nums[2]:
                answers.append([(nums[0], nums[1]), ["+", "-"][i], (a, nums[2]), ["+", "-"][j], (nums[0], b), ["+", "-"][k]])

# Print the first answer
for answer in answers:
    if answer[2][0] == answer[4][1] and answer[4][0] == answer[0][0]:
        print("{}{}{}={}{}{}".format(answer[0][0], answer[1], answer[0][1], answer[2][0], answer[3], answer[4][1]))
        break
