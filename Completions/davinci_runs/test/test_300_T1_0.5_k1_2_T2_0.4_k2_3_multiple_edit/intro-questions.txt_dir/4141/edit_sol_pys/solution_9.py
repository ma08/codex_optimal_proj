
input_num = int(input())
input_list = list(map(int, input().split()))

for num in input_list:
    if num % 2 == 0:
        if num % 3 != 0 and num % 5 != 0:
            print("DENIED")
            exit(0)
print("APPROVED")
