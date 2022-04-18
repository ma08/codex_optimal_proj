
n, l = map(int, input().split())

flavors = [l + i for i in range(n)]  # l+0, l+1, l+2 ... l+n

print(sum(flavors) - min([abs(f) for f in flavors]))  # sum(l+0, l+1, l+2 ... l+n) - min(|l+0|, |l+1|, |l+2| ... |l+n|)
