

num1 = input("Enter a number: ")
num2 = input("Enter a number: ")

list1 = [int(num1[2]), int(num1[1]), int(num1[0])]
list2 = [int(num2[2]), int(num2[1]), int(num2[0])]

if list1 > list2:
    print(list1[0], list1[1], list1[2])
else:
    print(list2[0], list2[1], list2[2])
