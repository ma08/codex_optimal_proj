

# cook your dish here
n = int(input())

def f(x):
    x = str(x)
    x = x.replace('0', '')
    x = int(x)
    x += 1
    return x

reachable = [n]
for i in range(1,10):
    reachable.append(f(reachable[-1]))
print(len(set(reachable)))