

# Solution

"""
The problem can be solved in $O(k \cdot n)$ time and $O(k)$ memory.

Let's iterate over the sequences one by one. Let's store the sum of the elements of the current sequence in a variable $s$.

Let's iterate over the elements of the current sequence one by one. Let's store the sum of the elements of the current sequence without the element we are currently iterating over in a variable $t$.

If there exists such a sequence $i$ and such an element $x$ that the sum $t$ equals to the sum of the elements of the $i$-th sequence without the element with index $x$, then we found the answer. Otherwise, we have to save the sum $t$ for the current sequence $i$.

We can store the sums for the previous sequences in a hash table. We will store the sum of the elements of the $i$-th sequence without the element with index $x$ as a key, and the pair $(i, x)$ as a value.

If we get the sum $t$ as a key in the hash table, then we found the answer. Otherwise, we have to update the hash table by adding the sum $t$ as a key and the pair $(i, x)$ as a value.

If we found the answer, we have to print it. Otherwise, we have to print "NO".
"""

k = int(input())

sum_ = []

for i in range(k):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    t = s
    for j in range(n):
        t -= a[j]
        if t in sum_:
            print("YES")
            print(sum_.index(t) + 1, j + 1)
            print(i + 1, j + 1)
            exit()
        sum_.append(t)

print("NO")
