

# gets the numbers from the user
num1 = int(input())
num2 = int(input())

# creates a list with the numbers in reverse order
list1 = [num1 % 10, (num1 // 10) % 10, num1 // 100]
list2 = [num2 % 10, (num2 // 10) % 10, num2 // 100]

# checks which number is greater
if list1[0] > list2[0]:
    print(str(list1[2]) + str(list1[1]) + str(list1[0]))
elif list1[0] == list2[0] and list1[1] > list2[1]:
    print(str(list1[2]) + str(list1[1]) + str(list1[0]))
elif list1[0] == list2[0] and list1[1] == list2[1] and list1[2] > list2[2]:
    print(str(list1[2]) + str(list1[1]) + str(list1[0]))
else:
    print(str(list2[2]) + str(list2[1]) + str(list2[0]))
