
n = int(input())
canisters = list(map(int, input().split()))

# Sort the canisters in descending order
canisters.sort(reverse=True)

print(canisters)
