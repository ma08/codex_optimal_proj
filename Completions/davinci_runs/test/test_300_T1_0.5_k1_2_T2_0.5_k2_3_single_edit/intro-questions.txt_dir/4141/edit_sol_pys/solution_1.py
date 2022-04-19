
num = int(input(""))
input_list = list(map(int, input().split()))
for i in input_list:
    if i % 2 == 0:
        if i % 3 == 0 or i % 5 == 0:
            continue
        else:
            print("DENIED") 
            exit()
print("APPROVED") 
