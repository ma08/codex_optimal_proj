# ABC081A
n = input()
print(n.count("1"))


# ABC081B

n = int(input())
a_list = list(map(int, input().split()))
count = 0

while all(a % 2 == 0 for a in a_list):
    a_list = [a / 2 for a in a_list]
    count += 1

print(count)
