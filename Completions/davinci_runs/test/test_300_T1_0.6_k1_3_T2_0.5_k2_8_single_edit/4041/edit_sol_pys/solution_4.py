

# get the input
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

# if there are no elements, the answer is 0
if len(a) == 0:
    print(0)

# if there is only one element, the answer is 1
elif len(a) == 1:
    print(1)

# otherwise, we need to find the longest increasing subsequence
else:
    # we'll keep track of the longest increasing subsequence so far
    best = 0

    # go through each element
    for i in range(n):
        # start a new subsequence with the current element
        # and assume it will be the longest
        best = 1
        current = 1

        # go through the rest of the elements
        for j in range(i + 1, n):
            # if the current element is less than the previous,
            # then the subsequence can be extended
            if a[j] > a[j - 1]:
                current += 1
                # if this is the longest subsequence so far,
                # update the best
                if current > best:
                    best = current

        # output the answer
        print(best)
