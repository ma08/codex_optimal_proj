

n = int(input())

def get_prefixes(s):
    return [s[:i] for i in range(1,len(s)+1)]

def get_suffixes(s):
    return [s[i:] for i in range(len(s))]

prefixes = []
suffixes = []

for _ in range(2*n-2):
    s = input()
    if len(s) == n:
        prefixes = get_prefixes(s)
        suffixes = get_suffixes(s)
    else:
        if len(s) in [len(p) for p in prefixes]:
            prefixes.remove(s)
        else:
            suffixes.remove(s)

for p in prefixes:
    print("P", end="")
for s in suffixes:
    print("S", end="")