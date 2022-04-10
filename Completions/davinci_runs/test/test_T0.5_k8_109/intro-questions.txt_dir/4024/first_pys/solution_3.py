

n, k = map(int,input().split())
s = input()

# n, k = 4, 5
# s = "asdf"

def get_subsequences(s):
    if len(s) == 0:
        return [""]
    else:
        subseqs = get_subsequences(s[1:])
        return subseqs + [s[0] + subseq for subseq in subseqs]

subseqs = get_subsequences(s)
subseqs.sort()

if len(subseqs) < k:
    print(-1)
else:
    total_cost = 0
    for subseq in subseqs[:k]:
        total_cost += n - len(subseq)
    print(total_cost)