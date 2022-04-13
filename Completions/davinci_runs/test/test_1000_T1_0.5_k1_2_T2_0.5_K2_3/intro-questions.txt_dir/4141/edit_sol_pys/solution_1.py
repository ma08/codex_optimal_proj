
num = int(input())
input_list = list(map(int, input().split())) #take input of numbers

for i in input_list: #loop to check if the number is divisible by 2
    if i % 2 == 0:
        if i % 3 != 0 and i % 5 != 0:
            print("DENIED")
            exit(0)
print("APPROVED")
