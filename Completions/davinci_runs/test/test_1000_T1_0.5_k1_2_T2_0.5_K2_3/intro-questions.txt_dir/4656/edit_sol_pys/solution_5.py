
# SOLUTION
# Find the largest substring that is K-beautiful
# The answer is the length of this substring

# Time: O(n)
# Space: O(1)

def get_beautiful_substring(s, k):
    if len(set(s)) == 1:
        return len(s)
    max_len = 0
    for i in range(len(s)):
        j = i
        while j < len(s)-1 and len(set(s[i:j+1])) == 1:
            j += 1
            if (j-i+1)%k == 0:
                max_len = max(j-i+1, max_len)
    return max_len

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    s = input()
    print(get_beautiful_substring(s, k))
