
n = int(input())
a = list(map(int, input().split()))

count = 0

while True:
    for i in range(n):
        if a[i] % 2 == 1:
            break
    else:
        count += 1
        a = [x / 2 for x in a]
        continue # continue は while の中で使える
    break # break は for の中で使える

print(count)
