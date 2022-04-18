

# gets the numbers from the user
num1 = input()
num2 = input()

# creates a list with the numbers in reverse order
list1 = [int(num1[2]), int(num1[1]), int(num1[0])]
list2 = [int(num2[2]), int(num2[1]), int(num2[0])]

#checks which number is greater
if list1 > list2:
    print(str(list1[0]) + str(list1[1]) + str(list1[2]))
else:
    print(str(list2[0]) + str(list2[1]) + str(list2[2]))
