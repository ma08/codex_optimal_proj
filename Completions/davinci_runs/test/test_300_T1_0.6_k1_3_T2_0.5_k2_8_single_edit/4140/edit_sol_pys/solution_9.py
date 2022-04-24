
a=[]
s = input()

# count the number of black tiles
counter = 0
for i in range(len(s)):
    if s[i]=='0':
        counter+=1
    else:
        a.append(counter)
        counter=0
a.append(counter)

# # count the number of black tiles but ignoring the beginning and ending of the string
# # this is done by counting the number of consecutive '0' characters starting from the beginning
# # and the number of consecutive '0' characters starting from the end
# # we take the maximum of the two
# counter_ignore_ends = 0
# counter_end = 0
# for c in s:
#     if c == '0':
#         counter_ignore_ends += 1
#     else:
#         break
# for c in reversed(s):
#     if c == '0':
#         counter_end += 1
#     else:
#         break
# counter_ignore_ends = max(counter_ignore_ends, counter_end)

# # the answer is the minimum of the two
# print(min(counter, counter_ignore_ends))

print(max(a))
