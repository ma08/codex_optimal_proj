
#
# Solution

n = int(input())

a = list(input().split())

a = [int(i) for i in a]

# print(a)

ind = [0]*n

for i in range(n):
    ind[a[i]-1] = i

# print(ind)

left = a[:]

right = a[:]

# print(left)

# print(right)


ans = ""

while len(left) > 0:
    if len(right) > 0:
        if ind[left[0]-1] < ind[right[0]-1]:
            ans += "L"
            left.pop(0)
        elif ind[left[0]-1] > ind[right[0]-1]:
            ans += "R"
            right.pop(0)
        else:
            if ind[left[-1]-1] < ind[right[0]-1]:
                ans += "L"
                left.pop(0)
            elif ind[left[-1]-1] > ind[right[0]-1]:
                ans += "R"
                right.pop(0)
            else:
                if left[0] > right[0]:
                    ans += "L"
                    left.pop(0)
                else:
                    ans += "R"
                    right.pop(0)
    else:
        ans += "L"
        left.pop(0)

print(len(ans))

print(ans)
