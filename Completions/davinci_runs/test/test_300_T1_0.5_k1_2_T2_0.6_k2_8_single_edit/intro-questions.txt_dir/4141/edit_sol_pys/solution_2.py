

input()
input_list = list(map(int, input().split()))

for n in input_list:
    if n % 2 == 0 and n % 3 != 0 and n % 5 != 0:
        print("DENIED")
        exit(0)
else:
    print("APPROVED")
