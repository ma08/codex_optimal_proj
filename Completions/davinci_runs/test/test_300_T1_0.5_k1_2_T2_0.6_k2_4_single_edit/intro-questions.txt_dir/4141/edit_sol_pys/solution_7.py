

num = int(input())
input_list = list(map(int, input().split()))
sum = 0
for i in range(num):
    sum += input_list[i]
if sum % 2 == 0:
    print("YES")
else:
    print("NO")
