

n = int(input())
nums = list(map(int, input().split()))

# 使用一个字典记录每个数字的个数，然后遍历字典，如果一个数字的个数大于n/2，那么它一定是最终结果的一个数字，
# 如果一个数字的个数小于n/2，那么它一定会被替换。

# 这里使用了collections.Counter()函数，它可以直接统计一个列表中每个元素的个数，并返回一个字典。
# 该函数自带了一个most_common()函数，可以直接返回一个字典中最常见的元素，这里我们只需要第一个元素即可。

from collections import Counter

counter = Counter(nums)

# 如果一个数字的个数大于n/2，那么它一定是最终结果的一个数字
for i in counter.most_common():
    if i[1] > n/2:
        num1 = i[0]
        break

# 如果一个数字的个数小于n/2，那么它一定会被替换
for i in counter.most_common():
    if i[1] < n/2:
        num2 = i[0]
        break

# 遍历列表，如果该元素不等于num1，那么它一定会被替换为num2
count = 0
for i in nums:
    if i != num1:
        count += 1

print(count)