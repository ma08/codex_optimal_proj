

n = int(input())
canisters = list(map(int, input().split()))

# Sort the canisters in descending order
canisters.sort(reverse=True)

# If the number of canisters is less than the number of balloons, it is impossible
if n < sum(canisters):
    print("impossible")

# If the number of canisters is equal to the number of balloons, the minimum fraction is 1
elif n == sum(canisters):
    print(1)

# If the number of canisters is greater than the number of balloons, we need to find the minimum fraction
else:
    max_fraction = sum(canisters) / n  # The maximum fraction is the sum of the canisters divided by the number of balloons
    min_fraction = canisters[0] / n   # The minimum fraction is the first canister divided by the number of balloons
    # The minimum fraction is the maximum fraction minus the difference between the maximum fraction and the minimum fraction
    # divided by the number of balloons minus the number of canisters
    min_fraction = max_fraction - (max_fraction - min_fraction) / (n - len(canisters))
    print(min_fraction)
