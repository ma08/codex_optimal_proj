
num = int(input())
input_list = list(map(int, input().split()))
for e in input_list:
    if e % 2 == 0:
        if e % 3 != 0 and e % 5 != 0:
            print("DENIED")
            exit(0)
print("APPROVED")
