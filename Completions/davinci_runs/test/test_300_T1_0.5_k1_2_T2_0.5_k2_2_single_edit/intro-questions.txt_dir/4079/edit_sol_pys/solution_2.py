

n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i in lst:
    if len(i) == len(set(i)):
        print("Yes")
    else:
        print("No")

# n = int(input())
# lst = [input() for _ in range(n)]
# for i in range(n):
#     if len(i) == len(set(i)) and len(set(i)) == ord(max(i)) - ord(min(i)) + 1:
#         print("Yes")
#     else:
#         print("No")
#
