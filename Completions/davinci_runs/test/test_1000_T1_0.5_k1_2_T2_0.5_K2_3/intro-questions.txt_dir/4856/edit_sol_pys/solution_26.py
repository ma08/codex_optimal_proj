

# gets the numbers from the user, and splits them into a list
num1 = input().split()
num2 = input().split()

# creates a list with the numbers in reverse order, and then sorts them
list1 = sorted([int(num1[2]), int(num1[1]), int(num1[0])], reverse=True)
list2 = sorted([int(num2[2]), int(num2[1]), int(num2[0])], reverse=True)

# checks which number is greater
if list1 > list2:
    print(str(list1[0]) + str(list1[1]) + str(list1[2]))
else:
    print(str(list2[0]) + str(list2[1]) + str(list2[2]))
