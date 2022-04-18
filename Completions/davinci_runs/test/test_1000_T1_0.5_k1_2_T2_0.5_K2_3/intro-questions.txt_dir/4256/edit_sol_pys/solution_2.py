A,B,C = map(int, input().split())

count = 0
while B >= A and count < C:
    B -= A
    count += 1
print(count)

# A,B,C = map(int, input().split())
#
# count = 0
# while B >= A:
#     B -= A
#     count += 1  # count = count + 1
#     if count == C:
#         break
#
# print(count)

count = 0
for i in range(C):
    if B >= A:
        B -= A
        count += 1
print(count)
