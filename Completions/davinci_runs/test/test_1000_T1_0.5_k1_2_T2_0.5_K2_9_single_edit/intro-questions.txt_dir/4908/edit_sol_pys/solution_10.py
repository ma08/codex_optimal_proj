
nums = [int(x) for x in input().split()]

for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if i == 0:
                a = "+"
            elif i == 1:
                a = "-"
            else:
                a = "*"
            if j == 0:
                b = "+"
            elif j == 1:
                b = "-"
            else:
                b = "*"
            if k == 0:
                c = "+"
            elif k == 1:
                c = "-"
            else:
                c = "*"
            if eval(str(nums[0]) + a + str(nums[1]) + b + str(nums[2]) + c + str(nums[3])) == nums[4]:
                print(str(nums[0]) + a + str(nums[1]) + b + str(nums[2]) + c + str(nums[3]) + "=" + str(nums[4]))
