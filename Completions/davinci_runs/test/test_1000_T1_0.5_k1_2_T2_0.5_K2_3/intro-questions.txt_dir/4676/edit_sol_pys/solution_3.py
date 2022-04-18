
odd = input()
even = input()

ans = ""
for i in range(len(odd)):
    ans += odd[i]
    if i < len(even):
        ans += even[i]

print(ans)
