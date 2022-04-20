

S, W = map(int, input().split())  # S: safe, W: weak

if W >= S:
    print("unsafe")
else:
    print("safe")
